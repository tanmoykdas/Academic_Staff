import socket
import threading
import struct
import time
import tkinter as tk
from tkinter import messagebox, scrolledtext
import sys
import os
from tkinter import ttk

try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

MCAST_GRP = '224.1.1.2'
MCAST_PORT = 5008
TOTAL_VOTERS = 5

votes = []
votes_lock = threading.Lock()

class ModernVotingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Election Voting System - Premium")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f2f5')
        
        self.setup_styles()
        self.setup_socket()
        self.create_widgets()
        self.running = True
        
        self.receiver_thread = threading.Thread(target=self.receive_votes_loop, daemon=True)
        self.receiver_thread.start()
        
        self.center_window()

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.style.configure('Title.TLabel', 
                           font=('Segoe UI', 24, 'bold'),
                           background='#f0f2f5',
                           foreground='#2c3e50')
        
        self.style.configure('Card.TFrame', 
                           background='white',
                           relief='raised',
                           borderwidth=1)
        
        self.style.configure('VoteCount.TLabel',
                           font=('Segoe UI', 16, 'bold'),
                           background='#f0f2f5',
                           foreground='#3498db')
        
        self.style.configure('Candidate.TButton',
                           font=('Segoe UI', 12, 'bold'),
                           padding=(20, 10))
        
        self.style.configure('Result.TLabel',
                           font=('Segoe UI', 18, 'bold'),
                           background='#f0f2f5')
        
        self.style.configure('Voter.TLabelframe',
                           font=('Segoe UI', 10, 'bold'),
                           background='white')
        
        self.style.configure('Voter.TLabelframe.Label',
                           font=('Segoe UI', 10, 'bold'),
                           background='white')

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def setup_socket(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            try:
                self.sock.bind(('', MCAST_PORT))
            except OSError:
                self.sock.bind((MCAST_GRP, MCAST_PORT))
            
            mreq = struct.pack("4sL", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
            self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
            self.sock.settimeout(1.0)
            
            self.send_sock = self.sock
        except Exception as e:
            messagebox.showerror("Network Error", f"Failed to setup multicast socket: {e}")
            sys.exit(1)

    def create_widgets(self):
        header_frame = ttk.Frame(self.root, style='Card.TFrame')
        header_frame.pack(fill='x', padx=20, pady=20)
        
        title_label = ttk.Label(header_frame, 
                               text="🗳️ Multicast Election Voting System", 
                               style='Title.TLabel')
        title_label.pack(pady=20)
        
        status_frame = ttk.Frame(self.root, style='Card.TFrame')
        status_frame.pack(fill='x', padx=20, pady=10)
        
        self.status_label = ttk.Label(status_frame, 
                                     text=f"Votes Received: 0/{TOTAL_VOTERS}", 
                                     style='VoteCount.TLabel')
        self.status_label.pack(pady=15)
        
        self.progress = ttk.Progressbar(status_frame, 
                                       orient='horizontal', 
                                       length=400, 
                                       mode='determinate',
                                       maximum=TOTAL_VOTERS)
        self.progress.pack(pady=10)
        
        self.voters_frame = ttk.Frame(self.root)
        self.voters_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.voter_panels = []
        for i in range(1, TOTAL_VOTERS + 1):
            panel = VoterPanel(self.voters_frame, i, self.send_sock)
            self.voter_panels.append(panel)
            
        results_frame = ttk.Frame(self.root, style='Card.TFrame')
        results_frame.pack(fill='x', padx=20, pady=20)
        
        ttk.Label(results_frame, 
                 text="Election Results", 
                 font=('Segoe UI', 16, 'bold'),
                 background='white').pack(pady=10)
        
        self.result_label = ttk.Label(results_frame, 
                                     text="Waiting for all votes...", 
                                     style='Result.TLabel',
                                     background='white')
        self.result_label.pack(pady=15)
        
        self.count_frame = ttk.Frame(results_frame, style='Card.TFrame')
        self.count_frame.pack(pady=10)
        
        self.count_label_a = ttk.Label(self.count_frame, 
                                      text="Candidate A: 0 votes", 
                                      font=('Segoe UI', 12),
                                      background='white',
                                      foreground='#e74c3c')
        self.count_label_a.grid(row=0, column=0, padx=20, pady=5)
        
        self.count_label_b = ttk.Label(self.count_frame, 
                                      text="Candidate B: 0 votes", 
                                      font=('Segoe UI', 12),
                                      background='white',
                                      foreground='#3498db')
        self.count_label_b.grid(row=0, column=1, padx=20, pady=5)

    def receive_votes_loop(self):
        while self.running:
            try:
                data, addr = self.sock.recvfrom(1024)
            except socket.timeout:
                continue
            except OSError:
                break
                
            try:
                text = data.decode('utf-8').strip()
            except Exception:
                continue

            electorate_id = None
            vote_val = None
            
            if text.startswith('E') and ':' in text:
                try:
                    left, vote_val = text.split(':', 1)
                    electorate_id = int(left[1:])
                    vote_val = vote_val.strip()
                except Exception:
                    vote_val = None
            else:
                if text in ('A', 'B'):
                    vote_val = text

            if vote_val in ('A', 'B'):
                with votes_lock:
                    votes.append(vote_val)
                    current_count = len(votes)

                display_msg = f"From {addr}: {text}"
                
                self.root.after(0, self.append_to_all_panels, display_msg)
                self.root.after(0, self.update_status, current_count)
                
                if current_count >= TOTAL_VOTERS:
                    self.root.after(0, self.compute_and_display_result)

    def append_to_all_panels(self, msg):
        for panel in self.voter_panels:
            panel.append_recv_message(msg)

    def update_status(self, count):
        self.status_label.config(text=f"Votes Received: {count}/{TOTAL_VOTERS}")
        self.progress['value'] = count
        
        count_a = votes.count('A')
        count_b = votes.count('B')
        self.count_label_a.config(text=f"Candidate A: {count_a} votes")
        self.count_label_b.config(text=f"Candidate B: {count_b} votes")

    def compute_and_display_result(self):
        with votes_lock:
            count_a = votes.count('A')
            count_b = votes.count('B')

        if count_a > count_b:
            winner_text = "🏆 Candidate A Wins!"
            color = "#e74c3c"
        elif count_b > count_a:
            winner_text = "🏆 Candidate B Wins!"
            color = "#3498db"
        else:
            winner_text = "🤝 It's a Tie!"
            color = "#f39c12"
            
        self.result_label.config(text=winner_text, foreground=color)

        for panel in self.voter_panels:
            panel.update_winner(winner_text)

        self.show_result_dialog(count_a, count_b, winner_text)

    def show_result_dialog(self, count_a, count_b, winner_text):
        result_window = tk.Toplevel(self.root)
        result_window.title("Election Results")
        result_window.geometry("400x300")
        result_window.configure(bg='#f0f2f5')
        result_window.transient(self.root)
        result_window.grab_set()
        
        result_window.update_idletasks()
        x = (result_window.winfo_screenwidth() // 2) - (400 // 2)
        y = (result_window.winfo_screenheight() // 2) - (300 // 2)
        result_window.geometry(f"400x300+{x}+{y}")
        
        ttk.Label(result_window, 
                 text="ELECTION RESULTS", 
                 font=('Segoe UI', 18, 'bold'),
                 background='#f0f2f5').pack(pady=20)
        
        count_frame = ttk.Frame(result_window, style='Card.TFrame')
        count_frame.pack(pady=10, padx=20, fill='x')
        
        ttk.Label(count_frame, 
                 text=f"Candidate A: {count_a} votes", 
                 font=('Segoe UI', 14),
                 background='white',
                 foreground='#e74c3c').pack(pady=10)
        
        ttk.Label(count_frame, 
                 text=f"Candidate B: {count_b} votes", 
                 font=('Segoe UI', 14),
                 background='white',
                 foreground='#3498db').pack(pady=10)
        
        ttk.Label(result_window, 
                 text=winner_text, 
                 font=('Segoe UI', 16, 'bold'),
                 background='#f0f2f5').pack(pady=20)
        
        ttk.Button(result_window, 
                  text="Close", 
                  command=result_window.destroy).pack(pady=20)

    def on_close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit the voting system?"):
            self.running = False
            try:
                mreq = struct.pack("4sL", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
                self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_DROP_MEMBERSHIP, mreq)
            except Exception:
                pass
            try:
                self.sock.close()
            except Exception:
                pass
            self.root.destroy()
            sys.exit(0)


class VoterPanel:
    def __init__(self, parent, idx, send_sock):
        self.idx = idx
        self.send_sock = send_sock
        self.voted = False
        self.vote_value = None
        
        self.frame = ttk.LabelFrame(parent, 
                                   text=f"Voter {idx}", 
                                   style='Voter.TLabelframe')
        self.frame.grid(row=0, column=idx-1, padx=10, pady=10, sticky='nsew')
        
        self.var = tk.StringVar(value="")
        
        vote_frame = ttk.Frame(self.frame)
        vote_frame.pack(fill='x', padx=10, pady=10)
        
        ttk.Radiobutton(vote_frame, 
                       text="Candidate A", 
                       variable=self.var, 
                       value="A").grid(row=0, column=0, sticky='w', padx=5)
        
        ttk.Radiobutton(vote_frame, 
                       text="Candidate B", 
                       variable=self.var, 
                       value="B").grid(row=1, column=0, sticky='w', padx=5)
        
        self.btn_cast = ttk.Button(vote_frame, 
                                  text="Cast Vote", 
                                  command=self.cast_vote,
                                  style='Candidate.TButton')
        self.btn_cast.grid(row=0, column=1, rowspan=2, padx=10)
        
        self.vote_status = ttk.Label(self.frame, 
                                    text="Not voted yet", 
                                    font=('Segoe UI', 10),
                                    foreground='blue')
        self.vote_status.pack(pady=5)
        
        ttk.Label(self.frame, 
                 text="Network Messages:").pack(anchor='w', padx=10)
        
        self.recv_text = scrolledtext.ScrolledText(self.frame, 
                                                  width=25, 
                                                  height=6, 
                                                  state='disabled',
                                                  font=('Consolas', 9))
        self.recv_text.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.winner_label = ttk.Label(self.frame, 
                                     text="Winner: Not decided", 
                                     font=('Segoe UI', 10, 'bold'),
                                     foreground='green',
                                     wraplength=200)
        self.winner_label.pack(pady=5)

    def append_recv_message(self, msg):
        self.recv_text.configure(state='normal')
        self.recv_text.insert(tk.END, msg + "\n")
        self.recv_text.yview_moveto(1.0)
        self.recv_text.configure(state='disabled')

    def cast_vote(self):
        if self.voted:
            messagebox.showwarning("Already Voted", f"Voter {self.idx} has already cast a vote.")
            return
            
        choice = self.var.get()
        if choice not in ('A', 'B'):
            messagebox.showwarning("No Selection", "Please select a candidate before casting your vote.")
            return

        msg = f"E{self.idx}:{choice}"
        try:
            self.send_sock.sendto(msg.encode('utf-8'), (MCAST_GRP, MCAST_PORT))
        except Exception as e:
            messagebox.showerror("Network Error", f"Failed to send vote: {e}")
            return
            
        self.voted = True
        self.vote_value = choice
        self.vote_status.config(text=f"Voted: {choice}", foreground='darkgreen')
        self.btn_cast.config(state='disabled')
        
        self.append_recv_message(f"Sent: {msg}")

    def update_winner(self, winner_text):
        self.winner_label.config(text=f"Winner: {winner_text}")


def main():
    root = tk.Tk()
    app = ModernVotingApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()


if __name__ == "__main__":
    main()