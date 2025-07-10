# Software Name: City_Mapper
# Category: Transportation
# Description: City Mapper is a transportation software application that helps users navigate and explore cities efficiently. It provides detailed information about various transportation modes and routes, including public transport, walking, and cycling. Users can input their starting point and destination, and City Mapper will calculate and display the optimal route options based on factors like distance, travel time, and user preferences. The application also offers real-time updates on traffic conditions, public transport schedules, and nearby points of interest.

import networkx as nx
import heapq

class CityMapper:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node_id, name, latitude, longitude):
        """Adds a location node to the city graph."""
        self.graph.add_node(node_id, name=name, latitude=latitude, longitude=longitude)

    def add_edge(self, start_node, end_node, mode, distance, time, cost=0):
        """Adds a transportation edge between two locations."""
        self.graph.add_edge(start_node, end_node, mode=mode, distance=distance, time=time, cost=cost)

    def calculate_route(self, start_node, end_node, preference="time"):
        """Calculates the optimal route based on user preference (time, distance, cost)."""
        try:
            if preference == "time":
                path = nx.shortest_path(self.graph, start_node, end_node, weight="time")
                total_time = nx.shortest_path_length(self.graph, start_node, end_node, weight="time")
                total_distance = sum(self.graph[path[i]][path[i+1]]['distance'] for i in range(len(path)-1))
                total_cost = sum(self.graph[path[i]][path[i+1]]['cost'] for i in range(len(path)-1))

            elif preference == "distance":
                path = nx.shortest_path(self.graph, start_node, end_node, weight="distance")
                total_distance = nx.shortest_path_length(self.graph, start_node, end_node, weight="distance")
                total_time = sum(self.graph[path[i]][path[i+1]]['time'] for i in range(len(path)-1))
                total_cost = sum(self.graph[path[i]][path[i+1]]['cost'] for i in range(len(path)-1))

            elif preference == "cost":
                # Dijkstra's algorithm with cost as the weight
                distances = {node: float('inf') for node in self.graph.nodes}
                distances[start_node] = 0
                priority_queue = [(0, start_node)]  # (cost, node)
                previous_nodes = {}

                while priority_queue:
                    cost, current_node = heapq.heappop(priority_queue)

                    if cost > distances[current_node]:
                        continue

                    for neighbor in self.graph.neighbors(current_node):
                        edge_cost = self.graph[current_node][neighbor]['cost']
                        new_cost = cost + edge_cost

                        if new_cost < distances[neighbor]:
                            distances[neighbor] = new_cost
                            priority_queue.append((new_cost, neighbor))
                            previous_nodes[neighbor] = current_node

                # Reconstruct path
                path = []
                current = end_node
                while current != start_node:
                    if current not in previous_nodes:
                        return None, None, None, None #No Path
                    path.insert(0, current)
                    current = previous_nodes[current]
                path.insert(0, start_node)

                total_cost = distances[end_node]
                total_distance = sum(self.graph[path[i]][path[i+1]]['distance'] for i in range(len(path)-1))
                total_time = sum(self.graph[path[i]][path[i+1]]['time'] for i in range(len(path)-1))

            else:
                raise ValueError("Invalid preference. Choose 'time', 'distance', or 'cost'.")

            return path, total_time, total_distance, total_cost

        except nx.NetworkXNoPath:
            return None, None, None, None

    def get_node_info(self, node_id):
        """Retrieves information about a specific location."""
        if node_id in self.graph.nodes:
            return self.graph.nodes[node_id]
        else:
            return None

    def update_traffic(self, start_node, end_node, delay):
      """Simulates traffic updates by adding a delay to the travel time."""
      if self.graph.has_edge(start_node, end_node):
          original_time = self.graph[start_node][end_node]['time']
          self.graph[start_node][end_node]['time'] = original_time + delay
      elif self.graph.has_edge(end_node, start_node):
           original_time = self.graph[end_node][start_node]['time']
           self.graph[end_node][start_node]['time'] = original_time + delay
      else:
          print(f"No route found between {start_node} and {end_node}")

    def display_route(self, path):
        """Displays the route in a user-friendly format."""
        if path:
            route_info = []
            for i in range(len(path) - 1):
                start_node = path[i]
                end_node = path[i+1]
                mode = self.graph[start_node][end_node]['mode']
                distance = self.graph[start_node][end_node]['distance']
                time = self.graph[start_node][end_node]['time']
                route_info.append(f"From {self.graph.nodes[start_node]['name']} to {self.graph.nodes[end_node]['name']} by {mode}: Distance={distance}, Time={time}")
            return route_info
        else:
            return "No route found."

if __name__ == '__main__':
    # Example Usage
    city_mapper = CityMapper()

    # Add locations
    city_mapper.add_node("A", "Town Hall", 34.0522, -118.2437)
    city_mapper.add_node("B", "Central Station", 34.0500, -118.2400)
    city_mapper.add_node("C", "Main Library", 34.0530, -118.2450)
    city_mapper.add_node("D", "Grand Park", 34.0510, -118.2500)


    # Add transportation routes
    city_mapper.add_edge("A", "B", "walking", 0.2, 3, 0)
    city_mapper.add_edge("A", "C", "walking", 0.1, 2, 0)
    city_mapper.add_edge("B", "C", "bus", 0.3, 5, 1)
    city_mapper.add_edge("B", "D", "train", 0.5, 7, 2)
    city_mapper.add_edge("C", "D", "walking", 0.4, 6, 0)


    # Calculate the best route (time)
    path, total_time, total_distance, total_cost = city_mapper.calculate_route("A", "D", "time")
    print("Route (Time):", city_mapper.display_route(path))
    print("Total Time:", total_time, "minutes")
    print("Total Distance:", total_distance, "km")
    print("Total Cost:", total_cost, "dollars")
    print("\n")


    # Calculate the best route (distance)
    path, total_time, total_distance, total_cost = city_mapper.calculate_route("A", "D", "distance")
    print("Route (Distance):", city_mapper.display_route(path))
    print("Total Time:", total_time, "minutes")
    print("Total Distance:", total_distance, "km")
    print("Total Cost:", total_cost, "dollars")
    print("\n")


    # Calculate the best route (cost)
    path, total_time, total_distance, total_cost = city_mapper.calculate_route("A", "D", "cost")
    print("Route (Cost):", city_mapper.display_route(path))
    print("Total Time:", total_time, "minutes")
    print("Total Distance:", total_distance, "km")
    print("Total Cost:", total_cost, "dollars")
    print("\n")


    # Update traffic conditions
    city_mapper.update_traffic("B", "C", 5)  # Add 5 minutes delay due to traffic

    # Recalculate route after traffic update
    path, total_time, total_distance, total_cost = city_mapper.calculate_route("A", "D", "time")
    print("Route (Time) after traffic update:", city_mapper.display_route(path))
    print("Total Time after traffic update:", total_time, "minutes")
    print("Total Distance after traffic update:", total_distance, "km")
    print("Total Cost after traffic update:", total_cost, "dollars")