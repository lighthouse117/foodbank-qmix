

def get_food_params(name):
    return food_params[name]


food_params = {
    "2a2f_p": {
        "n_agents": 2,
        "n_foods": 2,
        "initial_stock": [5, 5],
        "requests": [
            [2, 3],
            [3, 2],
        ],
    },
    "2a2f_c1": {
        "n_agents": 2,
        "n_foods": 2,
        "initial_stock": [5, 5],
        "requests": [
            [3, 10],
            [3, 10],
        ],
    },
    "2a3f_p": {
        "n_agents": 2,
        "n_foods": 3,
        "initial_stock": [10, 10, 10],
        "requests": [
            [5, 3, 9],
            [5, 7, 1],
        ],
    },
    "2a3f_c1": {
        "n_agents": 2,
        "n_foods": 3,
        "initial_stock": [10, 10, 10],
        "requests": [
            [6, 8, 10],
            [6, 8, 10],
        ],
    },
}
