def root(v, p):
    if p[v] == v:
        return v
    else:
        p[v] = root(p[v], p)  # Path compression
        return p[v]

def MST_kruskal(edges, n, k):
    F = []  # List to store MST edges
    p = {i: i for i in range(1, n + 1)}  # Parent dictionary for 1-based indexing

    # Process edges in sorted order
    for e in edges:
        u, v, w = e
        u_r = root(u, p)
        v_r = root(v, p)

        # Add edge if it doesn't create a cycle
        if u_r != v_r:
            F.append(e)
            p[u_r] = v_r  # Union

    # Ensure k <= len(F)
    if k > len(F):
        raise ValueError("k cannot be greater than the number of edges in the MST.")

    # Remove edges to split into k components
    while k > 1:
        max_element = max(F, key=lambda x: x[2])  # Edge with maximum weight
        F.remove(max_element)
        k -= 1

    # Calculate total weight of the MST
    S = sum(weight for _, _, weight in F)
    return F, S

def read_input():
    n, m, k = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    return n, m, k, edges

# Main logic
n, m, k, edges = read_input()

F, S = MST_kruskal(edges, n, k)

print(S)
