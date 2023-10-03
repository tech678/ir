# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 10:10:44 2023

@author: HARI PRIYA
"""

import numpy as np

def hits_algorithm(adjacency_matrix, max_iterations=100, tol=1e-6):
    num_nodes = adjacency_matrix.shape[0]

    # Initialize hub and authority scores
    hubs = np.ones(num_nodes)
    authorities = np.ones(num_nodes)

    for _ in range(max_iterations):
        # Update authority scores based on hub scores
        new_authorities = np.dot(adjacency_matrix.T, hubs)

        # Update hub scores based on authority scores
        new_hubs = np.dot(adjacency_matrix, authorities)

        # Normalize the scores
        norm_authorities = np.linalg.norm(new_authorities)
        norm_hubs = np.linalg.norm(new_hubs)

        authorities = new_authorities / norm_authorities
        hubs = new_hubs / norm_hubs
        
        # Round off values to 3 digits
        authorities = np.round(authorities,3)
        hubs = np.round(hubs,3)

        # Check for convergence
        if (np.all(np.abs(authorities - new_authorities) < tol) and
                np.all(np.abs(hubs - new_hubs) < tol)):
            break

    return authorities, hubs

# Create a simple adjacency matrix as an example
# adjacency_matrix = np.array([[0, 1, 1, 1], [0, 0, 1, 1], [0, 1, 0, 0], [1, 0, 1, 0]])
adjacency_matrix = np.array([[0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0],[0, 1, 1, 0, 0, 0, 0, 0],[0, 1, 1, 1, 0, 1, 0, 0],[0, 0, 1, 0, 0, 0, 0, 1],[1, 0, 1, 0, 0, 0, 0, 0],[1, 0, 0, 0, 0, 0, 0, 0]])

# Compute HITS scores
authorities, hubs = hits_algorithm(adjacency_matrix)

# Print the authorities and hubs scores
auth = {}
n = 65
for i in range(len(authorities)):
    auth[chr(n+i)] = authorities[i]

print("Authorities:",auth)

hub = {}
n = 65
for i in range(len(hubs)):
    hub[chr(n+i)] = hubs[i]

print("Hubs:",hub)

# Print the node with highest authority and hub score
max_auth_key = max(auth,key=auth.get)
max_auth_score = auth[max_auth_key]
print("Node",max_auth_key,"has maximum authority score of",max_auth_score)
max_hub_key = max(hub,key=hub.get)
max_hub_score = hub[max_hub_key]
print("Node",max_hub_key,"has maximum hub score of",max_hub_score)