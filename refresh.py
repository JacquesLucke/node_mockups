import bpy
import typing
from dataclasses import dataclass

def refresh_nodes():
    for tree in bpy.data.node_groups:
        state = get_tree_state(tree)

        for node in tree.nodes:
            node.refresh()

        restore_tree_state(tree, state)

@dataclass
class TreeState:
    links: typing.List["LinkState"]
    nodes: typing.List["NodeState"]

@dataclass
class LinkState:
    from_socket: "SocketID"
    to_socket: "SocketID"

@dataclass
class NodeState:
    name: str
    inputs: typing.List["SocketState"]
    outputs: typing.List["SocketState"]

@dataclass
class SocketState:
    socket_id: "SocketID"
    value: object

@dataclass
class SocketID:
    node_name: str
    socket_name: str
    is_output: bool

    def find(self, tree):
        try:
            node = tree.nodes[self.node_name]
            return self.find_in_node(node)
        except:
            return None

    def find_in_node(self, node):
        try:
            sockets = node.outputs if self.is_output else node.inputs
            return sockets[self.socket_name]
        except:
            return None

def get_tree_state(tree):
    return TreeState(
        [get_link_data(link) for link in tree.links],
        [get_node_state(node) for node in tree.nodes]
    )

def get_link_data(link):
    return LinkState(
        SocketID(link.from_node.name, link.from_socket.name, link.from_socket.is_output),
        SocketID(link.to_node.name, link.to_socket.name, link.to_socket.is_output))

def get_node_state(node):
    return NodeState(
        node.name,
        [get_socket_state(node, socket) for socket in node.inputs],
        [get_socket_state(node, socket) for socket in node.outputs]
    )

def get_socket_state(node, socket):
    return SocketState(
        SocketID(node.name, socket.name, socket.is_output),
        socket.get_property()
    )

def restore_tree_state(tree, state):
    for link_state in state.links:
        from_socket = link_state.from_socket.find(tree)
        to_socket = link_state.to_socket.find(tree)
        if from_socket and to_socket:
            tree.links.new(to_socket, from_socket)

    for node_state in state.nodes:
        node = tree.nodes.get(node_state.name)
        if node is None: continue
        for socket_state in node_state.inputs:
            socket = socket_state.socket_id.find_in_node(node)
            if socket is None: continue
            socket.set_property(socket_state.value)
        for socket_state in node_state.outputs:
            socket = socket_state.socket_id.find_in_node(node)
            if socket is None: continue
            socket.set_property(socket_state.value)

def register():
    bpy.app.timers.register(refresh_nodes)
