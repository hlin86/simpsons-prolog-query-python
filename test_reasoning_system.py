from reasoning_system import ProblemFormulator, SymbolicReasoner, ResultInterpreter

# Create instances of ProblemFormulator, SymbolicReasoner, and ResultInterpreter
problem_formulator = ProblemFormulator()
symbolic_reasoner = SymbolicReasoner("simpsons.pl")
result_interpreter = ResultInterpreter()

# Test queries
queries = [
    ("Is Lisa a daughter of Marge?", "daughter(lisa, marge)."),
    ("Is Bart a daughter of Marge?", "daughter(bart, marge)."),
    ("Is Bart a son of Homer?", "son(bart, homer)."),
    ("Is Maggie a granddaughter of Abe?", "grandparent(abe, maggie)."),
]

for problem, goal in queries:
    # Formulate the problem
    symbolic_representation = problem_formulator.formulate_problem(problem, goal)

    # Solve the problem
    result = symbolic_reasoner.solve_problem(symbolic_representation)

    # Interpret the result
    interpretation = result_interpreter.interpret_result(problem, result)

    print(interpretation)
