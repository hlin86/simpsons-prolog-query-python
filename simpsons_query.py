from pyswip import Prolog

# Create a Prolog object
prolog = Prolog()

# Load the knowledge base
prolog.consult("C:/Users/15109/AIEALabAudit/simpsons.pl")

# Query for the children of Homer
query = "parent(homer, X)"
children_of_homer = list(prolog.query(query))

# Print the results
for result in children_of_homer:
    print(result["X"])
