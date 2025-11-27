import tkinter as tk
from tkinter import ttk, messagebox
import math
import copy

class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.routing_table = {}
        self.distance_vector = {}
        self.neighbors = {}
        
    def initialize_routing_table(self, all_nodes):
        self.routing_table = {}
        self.distance_vector = {}
        
        for node in all_nodes:
            if node.name == self.name:
                self.routing_table[node.name] = (0, self.name)
                self.distance_vector[node.name] = 0
            elif node in self.neighbors:
                cost = self.neighbors[node]
                self.routing_table[node.name] = (cost, node.name)
                self.distance_vector[node.name] = cost
            else:
                self.routing_table[node.name] = (float('inf'), None)
                self.distance_vector[node.name] = float('inf')


class Edge:
    def __init__(self, node1, node2, cost):
        self.node1 = node1
        self.node2 = node2
        self.cost = cost


class DistanceVectorGUI:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Distance Vector Routing Algorithm Visualization")
        self.root.geometry("1400x900")
        self.root.configure(bg='#f0f0f0')
        
        self.nodes = []
        self.edges = []
        self.node_radius = 30
        self.selected_node = None
        self.animation_step = 0
        self.animation_history = []
        self.is_animating = False
        
        self.colors = {
            'bg': '#f0f0f0',
            'canvas_bg': '#ffffff',
            'node': '#4CAF50',
            'node_selected': '#2196F3',
            'edge': '#757575',
            'text': '#212121',
            'panel_bg': '#fafafa',
            'button': '#2196F3',
            'button_hover': '#1976D2',
            'accent': '#FF5722'
        }
        
        self.setup_ui()
        self.create_sample_network()
        
    def setup_ui(self):
        title_frame = tk.Frame(self.root, bg='#2196F3', height=60)
        title_frame.pack(fill=tk.X, side=tk.TOP)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame,
            text="Distance Vector Routing Algorithm Visualization",
            font=('Arial', 20, 'bold'),
            bg='#2196F3',
            fg='white'
        )
        title_label.pack(expand=True)
        
        main_container = tk.Frame(self.root, bg=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        left_panel = tk.Frame(main_container, bg=self.colors['canvas_bg'], relief=tk.RAISED, bd=2)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        canvas_label = tk.Label(
            left_panel,
            text="Network Topology",
            font=('Arial', 14, 'bold'),
            bg=self.colors['canvas_bg']
        )
        canvas_label.pack(pady=5)
        
        self.canvas = tk.Canvas(
            left_panel,
            bg='#ffffff',
            highlightthickness=1,
            highlightbackground='#e0e0e0'
        )
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        right_panel = tk.Frame(main_container, bg=self.colors['panel_bg'], width=400, relief=tk.RAISED, bd=2)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(5, 0))
        right_panel.pack_propagate(False)
        
        control_frame = tk.LabelFrame(
            right_panel,
            text="Controls",
            font=('Arial', 12, 'bold'),
            bg=self.colors['panel_bg'],
            fg=self.colors['text']
        )
        control_frame.pack(fill=tk.X, padx=10, pady=10)
        
        button_style = {
            'font': ('Arial', 10, 'bold'),
            'bg': self.colors['button'],
            'fg': 'white',
            'relief': tk.FLAT,
            'cursor': 'hand2',
            'padx': 10,
            'pady': 8
        }
        
        self.run_btn = tk.Button(
            control_frame,
            text="▶ Run Algorithm",
            command=self.run_algorithm,
            **button_style
        )
        self.run_btn.pack(fill=tk.X, padx=5, pady=3)
        
        self.step_btn = tk.Button(
            control_frame,
            text="⏭ Next Step",
            command=self.next_step,
            state=tk.DISABLED,
            font=('Arial', 10, 'bold'),
            bg=self.colors['button'],
            fg='white',
            relief=tk.FLAT,
            cursor='hand2',
            padx=10,
            pady=8
        )
        self.step_btn.pack(fill=tk.X, padx=5, pady=3)
        
        self.reset_btn = tk.Button(
            control_frame,
            text="⟲ Reset",
            command=self.reset_algorithm,
            font=('Arial', 10, 'bold'),
            bg='#FF5722',
            fg='white',
            relief=tk.FLAT,
            cursor='hand2',
            padx=10,
            pady=8
        )
        self.reset_btn.pack(fill=tk.X, padx=5, pady=3)
        
        self.clear_btn = tk.Button(
            control_frame,
            text="✖ Clear Network",
            command=self.clear_network,
            font=('Arial', 10, 'bold'),
            bg='#f44336',
            fg='white',
            relief=tk.FLAT,
            cursor='hand2',
            padx=10,
            pady=8
        )
        self.clear_btn.pack(fill=tk.X, padx=5, pady=3)
        
        edit_frame = tk.LabelFrame(
            right_panel,
            text="Edit Network",
            font=('Arial', 12, 'bold'),
            bg=self.colors['panel_bg'],
            fg=self.colors['text']
        )
        edit_frame.pack(fill=tk.X, padx=10, pady=10)
        
        add_node_frame = tk.Frame(edit_frame, bg=self.colors['panel_bg'])
        add_node_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Label(add_node_frame, text="Node Name:", bg=self.colors['panel_bg']).pack(side=tk.LEFT, padx=2)
        self.node_name_entry = tk.Entry(add_node_frame, width=10)
        self.node_name_entry.pack(side=tk.LEFT, padx=2)
        
        tk.Button(
            add_node_frame,
            text="Add Node",
            command=self.add_node_dialog,
            font=('Arial', 10, 'bold'),
            bg=self.colors['button'],
            fg='white',
            relief=tk.FLAT,
            cursor='hand2',
            padx=5,
            pady=3
        ).pack(side=tk.LEFT, padx=2)
        
        add_edge_frame = tk.Frame(edit_frame, bg=self.colors['panel_bg'])
        add_edge_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Label(add_edge_frame, text="From:", bg=self.colors['panel_bg']).grid(row=0, column=0, sticky='w', padx=2)
        self.edge_from = tk.Entry(add_edge_frame, width=5)
        self.edge_from.grid(row=0, column=1, padx=2)
        
        tk.Label(add_edge_frame, text="To:", bg=self.colors['panel_bg']).grid(row=0, column=2, sticky='w', padx=2)
        self.edge_to = tk.Entry(add_edge_frame, width=5)
        self.edge_to.grid(row=0, column=3, padx=2)
        
        tk.Label(add_edge_frame, text="Cost:", bg=self.colors['panel_bg']).grid(row=1, column=0, sticky='w', padx=2, pady=2)
        self.edge_cost = tk.Entry(add_edge_frame, width=5)
        self.edge_cost.grid(row=1, column=1, padx=2, pady=2)
        
        tk.Button(
            add_edge_frame,
            text="Add Edge",
            command=self.add_edge_dialog,
            font=('Arial', 10, 'bold'),
            bg=self.colors['button'],
            fg='white',
            relief=tk.FLAT,
            cursor='hand2',
            padx=5,
            pady=3
        ).grid(row=1, column=2, columnspan=2, padx=2, pady=2)
        
        status_frame = tk.LabelFrame(
            right_panel,
            text="Status",
            font=('Arial', 12, 'bold'),
            bg=self.colors['panel_bg'],
            fg=self.colors['text']
        )
        status_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.status_text = tk.Text(
            status_frame,
            height=6,
            wrap=tk.WORD,
            font=('Arial', 9),
            bg='white',
            relief=tk.FLAT,
            padx=5,
            pady=5
        )
        self.status_text.pack(fill=tk.X, padx=5, pady=5)
        
        table_frame = tk.LabelFrame(
            right_panel,
            text="Routing Tables",
            font=('Arial', 12, 'bold'),
            bg=self.colors['panel_bg'],
            fg=self.colors['text']
        )
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        canvas_scroll = tk.Canvas(table_frame, bg=self.colors['panel_bg'])
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=canvas_scroll.yview)
        self.routing_table_frame = tk.Frame(canvas_scroll, bg=self.colors['panel_bg'])
        
        canvas_scroll.create_window((0, 0), window=self.routing_table_frame, anchor="nw")
        canvas_scroll.configure(yscrollcommand=scrollbar.set)
        
        canvas_scroll.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.routing_table_frame.bind(
            "<Configure>",
            lambda e: canvas_scroll.configure(scrollregion=canvas_scroll.bbox("all"))
        )
        
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        
        self.update_status("Welcome! Add nodes and edges to create a network, then run the Distance Vector algorithm.")
    
    def create_sample_network(self):
        node_a = Node("A", 200, 150)
        node_b = Node("B", 400, 100)
        node_c = Node("C", 400, 250)
        node_d = Node("D", 600, 150)
        
        self.nodes = [node_a, node_b, node_c, node_d]
        
        self.add_edge(node_a, node_b, 1)
        self.add_edge(node_a, node_c, 4)
        self.add_edge(node_b, node_c, 2)
        self.add_edge(node_b, node_d, 5)
        self.add_edge(node_c, node_d, 1)
        
        self.draw_network()
        self.update_status("Sample network loaded. Click 'Run Algorithm' to start the Distance Vector simulation.")
    
    def add_edge(self, node1, node2, cost):
        edge = Edge(node1, node2, cost)
        self.edges.append(edge)
        
        node1.neighbors[node2] = cost
        node2.neighbors[node1] = cost
    
    def draw_network(self):
        self.canvas.delete("all")
        
        for edge in self.edges:
            x1, y1 = edge.node1.x, edge.node1.y
            x2, y2 = edge.node2.x, edge.node2.y
            
            self.canvas.create_line(
                x1, y1, x2, y2,
                fill=self.colors['edge'],
                width=2,
                tags="edge"
            )
            
            mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
            self.canvas.create_oval(
                mid_x - 15, mid_y - 15, mid_x + 15, mid_y + 15,
                fill='#FFC107',
                outline='#FFA000',
                width=2,
                tags="cost"
            )
            self.canvas.create_text(
                mid_x, mid_y,
                text=str(edge.cost),
                font=('Arial', 10, 'bold'),
                fill='#000000',
                tags="cost"
            )
        
        for node in self.nodes:
            color = self.colors['node_selected'] if node == self.selected_node else self.colors['node']
            
            self.canvas.create_oval(
                node.x - self.node_radius, node.y - self.node_radius,
                node.x + self.node_radius, node.y + self.node_radius,
                fill=color,
                outline='#388E3C',
                width=3,
                tags=f"node_{node.name}"
            )
            
            self.canvas.create_text(
                node.x, node.y,
                text=node.name,
                font=('Arial', 16, 'bold'),
                fill='white',
                tags=f"node_{node.name}"
            )
    
    def on_canvas_click(self, event):
        x, y = event.x, event.y
        
        for node in self.nodes:
            distance = math.sqrt((x - node.x)**2 + (y - node.y)**2)
            if distance <= self.node_radius:
                self.selected_node = node
                self.draw_network()
                self.display_routing_tables()
                return
        
        self.selected_node = None
        self.draw_network()
    
    def add_node_dialog(self):
        name = self.node_name_entry.get().strip().upper()
        
        if not name:
            messagebox.showwarning("Warning", "Please enter a node name!")
            return
        
        if any(node.name == name for node in self.nodes):
            messagebox.showwarning("Warning", f"Node {name} already exists!")
            return
        
        import random
        x = random.randint(100, 700)
        y = random.randint(100, 400)
        
        node = Node(name, x, y)
        self.nodes.append(node)
        
        self.node_name_entry.delete(0, tk.END)
        self.draw_network()
        self.update_status(f"Node {name} added at ({x}, {y})")
    
    def add_edge_dialog(self):
        from_name = self.edge_from.get().strip().upper()
        to_name = self.edge_to.get().strip().upper()
        
        try:
            cost = int(self.edge_cost.get().strip())
            if cost <= 0:
                raise ValueError()
        except:
            messagebox.showwarning("Warning", "Please enter a valid positive cost!")
            return
        
        node1 = next((n for n in self.nodes if n.name == from_name), None)
        node2 = next((n for n in self.nodes if n.name == to_name), None)
        
        if not node1 or not node2:
            messagebox.showwarning("Warning", "Both nodes must exist!")
            return
        
        if node1 == node2:
            messagebox.showwarning("Warning", "Cannot create self-loop!")
            return
        
        for edge in self.edges:
            if (edge.node1 == node1 and edge.node2 == node2) or \
               (edge.node1 == node2 and edge.node2 == node1):
                messagebox.showwarning("Warning", "Edge already exists!")
                return
        
        self.add_edge(node1, node2, cost)
        
        self.edge_from.delete(0, tk.END)
        self.edge_to.delete(0, tk.END)
        self.edge_cost.delete(0, tk.END)
        
        self.draw_network()
        self.update_status(f"Edge added: {from_name} ↔ {to_name} (cost: {cost})")
    
    def clear_network(self):
        if messagebox.askyesno("Confirm", "Clear the entire network?"):
            self.nodes = []
            self.edges = []
            self.selected_node = None
            self.animation_step = 0
            self.animation_history = []
            self.is_animating = False
            
            self.canvas.delete("all")
            self.update_status("Network cleared.")
            self.display_routing_tables()
    
    def run_algorithm(self):
        if len(self.nodes) == 0:
            messagebox.showwarning("Warning", "Please add nodes to the network first!")
            return
        
        self.update_status("Initializing Distance Vector algorithm...")
        
        for node in self.nodes:
            node.initialize_routing_table(self.nodes)
        
        self.animation_history = []
        converged = False
        iteration = 0
        max_iterations = len(self.nodes) - 1
        
        self.animation_history.append({
            'iteration': 0,
            'message': 'Initial state - Each node knows only its direct neighbors',
            'tables': self.get_routing_tables_snapshot()
        })
        
        while not converged and iteration < max_iterations:
            iteration += 1
            converged = True
            
            updates = {}
            
            for node in self.nodes:
                updates[node] = {}
                
                for dest_node in self.nodes:
                    dest_name = dest_node.name
                    current_cost = node.distance_vector.get(dest_name, float('inf'))
                    best_cost = current_cost
                    best_next_hop = node.routing_table[dest_name][1]
                    
                    for neighbor, link_cost in node.neighbors.items():
                        if dest_name in neighbor.distance_vector:
                            new_cost = link_cost + neighbor.distance_vector[dest_name]
                            
                            if new_cost < best_cost:
                                best_cost = new_cost
                                best_next_hop = neighbor.name
                    
                    if best_cost < current_cost:
                        updates[node][dest_name] = (best_cost, best_next_hop)
                        converged = False
            
            for node, node_updates in updates.items():
                for dest_name, (cost, next_hop) in node_updates.items():
                    node.routing_table[dest_name] = (cost, next_hop)
                    node.distance_vector[dest_name] = cost
            
            if not converged:
                self.animation_history.append({
                    'iteration': iteration,
                    'message': f'Iteration {iteration} - Nodes exchange distance vectors and update routing tables',
                    'tables': self.get_routing_tables_snapshot()
                })
        
        self.animation_history.append({
            'iteration': iteration + 1,
            'message': 'Algorithm converged! All routing tables are optimal.',
            'tables': self.get_routing_tables_snapshot()
        })
        
        self.animation_step = 0
        self.is_animating = True
        self.step_btn.config(state=tk.NORMAL)
        self.run_btn.config(state=tk.DISABLED)
        
        self.next_step()
    
    def next_step(self):
        if self.animation_step >= len(self.animation_history):
            self.update_status("Animation complete! Algorithm has converged.")
            self.step_btn.config(state=tk.DISABLED)
            self.run_btn.config(state=tk.NORMAL)
            return
        
        step_data = self.animation_history[self.animation_step]
        
        message = f"Step {self.animation_step + 1}/{len(self.animation_history)}: {step_data['message']}"
        self.update_status(message)
        
        self.restore_routing_tables_snapshot(step_data['tables'])
        
        self.display_routing_tables()
        
        self.animation_step += 1
    
    def get_routing_tables_snapshot(self):
        snapshot = {}
        for node in self.nodes:
            snapshot[node.name] = copy.deepcopy(node.routing_table)
        return snapshot
    
    def restore_routing_tables_snapshot(self, snapshot):
        for node in self.nodes:
            if node.name in snapshot:
                node.routing_table = copy.deepcopy(snapshot[node.name])
    
    def reset_algorithm(self):
        self.animation_step = 0
        self.animation_history = []
        self.is_animating = False
        self.step_btn.config(state=tk.DISABLED)
        self.run_btn.config(state=tk.NORMAL)
        
        for node in self.nodes:
            node.routing_table = {}
            node.distance_vector = {}
        
        self.display_routing_tables()
        self.update_status("Algorithm reset. Click 'Run Algorithm' to start again.")
    
    def display_routing_tables(self):
        for widget in self.routing_table_frame.winfo_children():
            widget.destroy()
        
        if not self.nodes:
            return
        
        for node in self.nodes:
            node_frame = tk.Frame(self.routing_table_frame, bg='#e3f2fd', relief=tk.RAISED, bd=2)
            node_frame.pack(fill=tk.X, padx=5, pady=5)
            
            header = tk.Label(
                node_frame,
                text=f"Node {node.name}",
                font=('Arial', 11, 'bold'),
                bg='#2196F3',
                fg='white',
                pady=3
            )
            header.pack(fill=tk.X)
            
            if not node.routing_table:
                tk.Label(
                    node_frame,
                    text="Not initialized",
                    font=('Arial', 9),
                    bg='#e3f2fd'
                ).pack(pady=5)
                continue
            
            table_frame = tk.Frame(node_frame, bg='#e3f2fd')
            table_frame.pack(fill=tk.X, padx=5, pady=5)
            
            tk.Label(table_frame, text="Dest", font=('Arial', 9, 'bold'), bg='#e3f2fd', width=6).grid(row=0, column=0, padx=2, pady=2)
            tk.Label(table_frame, text="Cost", font=('Arial', 9, 'bold'), bg='#e3f2fd', width=6).grid(row=0, column=1, padx=2, pady=2)
            tk.Label(table_frame, text="Next Hop", font=('Arial', 9, 'bold'), bg='#e3f2fd', width=10).grid(row=0, column=2, padx=2, pady=2)
            
            row = 1
            for dest, (cost, next_hop) in sorted(node.routing_table.items()):
                cost_str = "∞" if cost == float('inf') else str(cost)
                next_hop_str = "-" if next_hop is None else next_hop
                
                tk.Label(table_frame, text=dest, font=('Arial', 9), bg='white', relief=tk.FLAT, width=6).grid(row=row, column=0, padx=2, pady=1)
                tk.Label(table_frame, text=cost_str, font=('Arial', 9), bg='white', relief=tk.FLAT, width=6).grid(row=row, column=1, padx=2, pady=1)
                tk.Label(table_frame, text=next_hop_str, font=('Arial', 9), bg='white', relief=tk.FLAT, width=10).grid(row=row, column=2, padx=2, pady=1)
                row += 1
    
    def update_status(self, message):
        self.status_text.config(state=tk.NORMAL)
        self.status_text.delete(1.0, tk.END)
        self.status_text.insert(1.0, message)
        self.status_text.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    app = DistanceVectorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
