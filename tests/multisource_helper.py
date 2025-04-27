import array

_show_dbg_info = True


def build_adj_list_pa1(n, edges):
    # Builds an adjacency list
    adj_list = [array.array('I') for _ in range(n)]

    for (i, j) in edges:
        adj_list[i].append(j)
        adj_list[j].append(i)

    return adj_list


def connected_to_pa1(n, edges, src):
    adj_list = build_adj_list_pa1(n, edges)

    # Boolean vector indicating which vertices
    # are connected
    visited = array.array('b', n * [False])
    # Stack for DFS
    stack = array.array('I', [src])

    while stack:
        v = stack.pop()
        if visited[v]:
            continue
        visited[v] = True
        for succ in adj_list[v]:
            if not visited[succ]:
                stack.append(succ)

    return [i for i in range(n) if visited[i]]


def evaluate_pa1_4(n, edges, src, v_list):
    if len(set(v_list)) != len(v_list):
        if _show_dbg_info:
            print("Elements in iterable not unique")
        return False

    v_list = tuple(sorted(v_list))
    my_list = tuple(sorted(connected_to_pa1(n, edges, src)))

    if v_list != my_list:
        if _show_dbg_info:
            print(f"For\n n={n}\n edges={edges} \n src={src}")
            print(f"expected : {my_list}")
            print(f"obtained : {v_list}")
        return False
    return True


class OpCount(object):
    def __init__(self):
        self.__counter = 0

    def reset(self):
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def __call__(self, *args, **kwargs):
        self.__counter += 1


class OpAdd(OpCount):
    @staticmethod
    def neutral():
        return 0

    def __call__(self, v1, v2):
        super().__call__()
        return v1 + v2


class OpMul(OpCount):
    @staticmethod
    def neutral():
        return 1

    def __call__(self, v1, v2):
        super().__call__()
        return v1 * v2


class OpAnd(OpCount):
    @staticmethod
    def neutral():
        return True

    def __call__(self, v1, v2):
        super().__call__()
        return bool(v1) and bool(v2)


class OpOr(OpCount):
    @staticmethod
    def neutral():
        return False

    def __call__(self, v1, v2):
        super().__call__()
        return bool(v1) or bool(v2)


class OpMin(OpCount):
    @staticmethod
    def neutral():
        from math import inf
        return inf

    def __call__(self, v1, v2):
        super().__call__()
        return min(v1, v2)


class OpMax(OpCount):
    @staticmethod
    def neutral():
        from math import inf
        return -inf

    def __call__(self, v1, v2):
        super().__call__()
        return max(v1, v2)


op_add = OpAdd()
op_mul = OpMul()
op_min = OpMin()
op_max = OpMax()
op_and = OpAnd()
op_or = OpOr()

all_op = [op_add, op_mul, op_min, op_max, op_and, op_or]


def init_mat_pa_g(n, edges, op_plus, e_plus, op_times, e_times):
    # Set up the matrix
    M = [[e_plus for _ in range(n)] for _ in range(n)]
    # Matrix for the successors of each vertex
    Succ = [[None for _ in range(n)] for _ in range(n)]

    # Diag elems
    for i in range(n):
        M[i][i] = e_times
        # From a variable type point of view we should do
        # M[i][i] = op_plus(op_plus.neutral(), op_times.neutral())
        Succ[i][i] = i

    # Add the edges
    # Set of the monoid is given in w
    for (a, b, w) in edges:
        v_before = M[a][b]
        M[a][b] = op_plus(w, M[a][b])
        # From a variable type point of view we should do
        # M[a][b] = op_plus(op_plus.neutral(),
        #     op_times(op_times.neutral(), w)
        if v_before != M[a][b]:
            Succ[a][b] = b

    return M, Succ


def init_mat_pa(n, edges, op_plus, op_times):
    return init_mat_pa_g(n, edges, op_plus, op_plus.neutral(), op_times, op_times.neutral())


def floyd_warshall_pa1(n, edges, op_plus, e_plus, op_times, e_times):
    # Generalised Floyd-Warshall algorithm

    M_last, _ = init_mat_pa(n, edges, op_plus, op_times)

    # Floyd-Warshall triple loop
    for k in range(n):
        M_current = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                M_current[i][j] = op_plus(M_last[i][j], op_times(M_last[i][k], M_last[k][j]))
        M_last = M_current

    return M_current


def floyd_warshall_pa2(n, edges, op_plus, e_plus, op_times, e_times):
    # Generalised Floyd-Warshall algorithm
    # Inplace and transposed

    M, _ = init_mat_pa(n, edges, op_plus, op_times)

    # Floyd-Warshall triple loop
    for k in range(n):
        for j in range(n):
            for i in range(n):
                M[i][j] = op_plus(M[i][j], op_times(M[i][k], M[k][j]))

    return M


def floyd_warshall_with_succ_pa1_g(n, edges, op_plus, e_plus, op_times, e_times):
    # Generalised Floyd-Warshall algorithm
    # with successor computation

    M_last, Succ = init_mat_pa_g(n, edges, op_plus, e_plus, op_times, e_times)

    # Floyd-Warshall triple loop
    for k in range(n):
        M_current = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                M_current[i][j] = op_plus(M_last[i][j], op_times(M_last[i][k], M_last[k][j]))
                # Check if changed
                if M_current[i][j] != M_last[i][j]:
                    Succ[i][j] = Succ[i][k]
        M_last = M_current

    return M_current, Succ


def floyd_warshall_with_succ_pa1(n, edges, op_plus, op_times):
    return floyd_warshall_with_succ_pa1_g(n, edges, op_plus, op_plus.neutral(),
                                          op_times, op_times.neutral())


def floyd_warshall_with_succ_pa2_g(n, edges, op_plus, e_plus, op_times, e_times):
    # Generalised Floyd-Warshall algorithm
    # with successor computation
    # Inplace and transposed
    from copy import deepcopy

    M, Succ = init_mat_pa_g(n, edges, op_plus, e_plus, op_times, e_times)

    # Floyd-Warshall triple loop
    for k in range(n):
        for j in range(n):
            for i in range(n):
                Mij = deepcopy(M[i][j])
                M[i][j] = op_plus(M[i][j], op_times(M[i][k], M[k][j]))
                # Check if changed
                if M[i][j] != Mij:
                    Succ[i][j] = Succ[i][k]

    return M, Succ


def floyd_warshall_with_succ_pa2(n, edges, op_plus, op_times):
    return floyd_warshall_with_succ_pa2_g(n, edges, op_plus, op_plus.neutral(),
                                          op_times, op_times.neutral())


def path_i2j_pa1(succ, i, j):
    assert len(succ) == len(succ[0])
    assert (0 <= i < len(succ)) and (0 <= j < len(succ))

    if succ[i][j] is None:
        return []

    path = [i]
    while i != j:
        i = succ[i][j]
        if (i in path) or (i is None):
            # Loop
            # Necessary for random graph generation
            return None
        path.append(i)
    return path


def safest_path_i2j_pa(n, edges, i, j):
    M, S = floyd_warshall_with_succ_pa1_g(n, edges, op_max, 0., op_mul, 1.)
    return path_i2j_pa1(S, i, j)


def rand_graph():
    # Generates a graph without "negative" loops
    import random
    random.seed()

    idem_pot_op = [op_min, op_max]

    while True:

        while True:
            op_plus = random.choice(idem_pot_op)
            op_times = random.choice(all_op)
            if type(op_plus) != type(op_times):
                break

        n = random.randint(10, 20)
        edges_dict = {}
        for _ in range(int(random.uniform(0.1, 0.5) * n * n)):
            while True:
                w = random.randint(-3, 15)
                if w != 0:
                    break
            while True:
                src = random.randint(0, n - 1)
                dst = random.randint(0, n - 1)
                if src != dst:
                    break

            edges_dict[(src, dst)] = w

        edges = [(a, b, w) for ((a, b), w) in edges_dict.items()]

        # Check if ok
        try:
            M1, D1 = floyd_warshall_with_succ_pa1(n, edges, op_plus, op_times)
            M2, D2 = floyd_warshall_with_succ_pa2(n, edges, op_plus, op_times)

            is_ok = True
            for i in range(n):
                if M1[i][i] != op_plus(op_plus.neutral(), op_times.neutral()):
                    is_ok = False
                    break
            for i in range(n):
                if not is_ok:
                    break
                for j in range(n):
                    if M1[i][j] != M2[i][j]:
                        print("Distances not equal")
                        is_ok = False
                        print_mat(M1)
                        print_mat(M2)
                        break
                    if path_i2j_pa1(D1, i, j) is None:
                        is_ok = False
                        break
                    if path_i2j_pa1(D2, i, j) is None:
                        is_ok = False
                        break
            if is_ok:
                return n, edges, op_plus, op_times
        except:
            pass


def rand_graph_safety():
    # Generates a graph without "negative" loops
    import random
    random.seed()

    op_plus = op_max
    op_times = op_mul

    while True:

        n = random.randint(4, 10)
        edges_dict = {}
        for _ in range(int(random.uniform(0.2, 0.8) * n * n)):
            w = random.random()
            while True:
                src = random.randint(0, n - 1)
                dst = random.randint(0, n - 1)
                if src != dst:
                    break
            edges_dict[(src, dst)] = w

        edges = [(a, b, w) for ((a, b), w) in edges_dict.items()]

        # Check if ok
        try:
            M1, D1 = floyd_warshall_with_succ_pa1_g(n, edges, op_plus, 0., op_times, 1.)
            M2, D2 = floyd_warshall_with_succ_pa2_g(n, edges, op_plus, 0., op_times, 1.)

            is_ok = True
            for i in range(n):
                if M1[i][i] != 1.:
                    is_ok = False
                    break
            for i in range(n):
                if not is_ok:
                    break
                for j in range(n):
                    if abs(M1[i][j] - M2[i][j]) > 1.e-12:
                        print("Distances not equal")
                        is_ok = False
                        print_mat(M1)
                        print_mat(M2)
                        break
                    if path_i2j_pa1(D1, i, j) is None:
                        is_ok = False
                        break
                    if path_i2j_pa1(D2, i, j) is None:
                        is_ok = False
                        break

            if is_ok:
                return n, edges, op_plus, op_times
        except:
            pass


def evaluate_safest_path_random(path_st):
    n, edges, this_plus, this_times = rand_graph_safety()

    M, S = floyd_warshall_with_succ_pa1_g(n, edges, op_max, 0., op_mul, 1.)

    ed = get_edge_dict_safety(edges)
    for i in range(n):
        for j in range(n):
            ij_path_st = path_st(n, edges, i, j)
            w = 1 if len(ij_path_st) > 0 else 0
            if len(ij_path_st) >= 2:
                for (src, dst) in zip(ij_path_st[:-1], ij_path_st[1:]):
                    try:
                        w *= ed[(src, dst)]
                    except KeyError:
                        return False
            if abs(w - M[i][j]) > 1e-12:
                return False
    return True


def __get_edge_dict(edges):
    ed = {}
    for (a, b, w) in edges:
        ed[(a, b)] = w
    return ed


def get_edge_dict_safety(edges):
    ed = {}
    for (a, b, w) in edges:
        ed[(a, b)] = max(w, ed.get((a, b), w))
    return ed


def __check_counters(n, edges, counters):
    return True  # Disable this check
    n_e = len(edges)
    possible_counters = []
    # Pure FW, init with neutral
    possible_counters.append((n ** 3, n ** 3))
    # Using it partially in init
    # Setting edges with plus
    possible_counters.append((n ** 3 + n_e, n ** 3))
    # Setting edges with plus and times
    possible_counters.append((n ** 3 + n_e, n ** 3 + n_e))
    # Setting diags with plus
    possible_counters.append((n ** 3 + n, n ** 3))
    # Setting edges with plus diags with plus
    possible_counters.append((n ** 3 + n_e + n, n ** 3))
    # Setting edges with plus and times diags with plus
    possible_counters.append((n ** 3 + n_e + n, n ** 3 + n_e))

    return counters in possible_counters


def evaluate_pa1_7(n, edges, op_plus, e_plus, op_times, e_times, fw_st):
    op_plus.reset()
    op_times.reset()

    M_pa1 = floyd_warshall_pa1(n, edges, op_plus, e_plus, op_times, e_times)
    counters_pa1 = (op_plus.get_counter(), op_times.get_counter())

    op_plus.reset()
    op_times.reset()
    M_st = fw_st(n, edges, op_plus, e_plus, op_times, e_times)
    counters_st = (op_plus.get_counter(), op_times.get_counter())
    # COUNTER check
    # if not __check_counters(n, edges, counters_st):
    #   return False

    if (len(M_pa1) != len(M_st)) or (len(M_pa1[0]) != len(M_st[0])):
        return False

    for i in range(len(M_pa1)):
        for j in range(len(M_pa1[0])):
            if M_st[i][j] != M_pa1[i][j]:
                return False

    return True


def evaluate_random(fw_st):
    n, edges, this_plus, this_times = rand_graph()

    return evaluate_pa1_7(n, edges, this_plus, this_plus.neutral(), this_times, this_times.neutral(), fw_st)


def evaluate_path_pa1(n, edges, op_plus, e_plus, op_times, e_times, fw_st, path_st):
    op_plus.reset()
    op_times.reset()

    M_pa1, D_pa1 = floyd_warshall_with_succ_pa1_g(n, edges, op_plus, e_plus, op_times, e_times)
    assert (__check_counters(n, edges, (op_plus.get_counter(), op_times.get_counter()))), \
        "Correct counter not admissible"

    op_plus.reset()
    op_times.reset()
    M_st, D_st = fw_st(n, edges, op_plus, e_plus, op_times, e_times)
    counters_st = (op_plus.get_counter(), op_times.get_counter())

    # if counters_pa1 != counters_st:
    # COUNTER check
    # if not __check_counters(n, edges, counters_st):
    #   return False

    if (len(M_pa1) != len(M_st)) or (len(M_pa1[0]) != len(M_st[0])):
        return False

    ed = __get_edge_dict(edges)
    for i in range(len(M_pa1)):
        for j in range(len(M_pa1[0])):
            # Check weight
            if M_st[i][j] != M_pa1[i][j]:
                return False
            # Check path
            ij_path_pa = tuple(path_i2j_pa1(D_pa1, i, j))
            ij_path_st = tuple(path_st(D_st, i, j))
            if len(ij_path_st) < 2:
                if len(ij_path_st) != len(ij_path_pa):
                    return False
            else:
                w_tot = op_times.neutral()
                # Type adjust
                w_tot = op_plus(op_plus.neutral(), op_times(op_times.neutral(), w_tot))
                for (src, dst) in zip(ij_path_st[:-1], ij_path_st[1:]):
                    try:
                        w = ed[(src, dst)]
                    except KeyError:
                        # Nonexistent edge
                        return False
                    w_tot = op_plus(op_plus.neutral(), op_times(w_tot, w))
                # if w_tot != M_st[i][j]:
                if op_plus(op_plus.neutral(), op_times(op_times.neutral(), w_tot)) != \
                        op_plus(op_plus.neutral(), op_times(op_times.neutral(), M_st[i][j])):
                    return False

    return True


def evaluate_path_random(fw_st, path_st):
    n, edges, this_plus, this_times = rand_graph()

    res = evaluate_path_pa1(n, edges, this_plus, this_plus.neutral(), this_times, this_times.neutral(), fw_st, path_st)

    return res


def print_mat(M):
    n = len(M)
    assert len(M) == len(M[0]), 'Dist mat not square'
    t_str = ""
    for i in range(n):
        for j in range(n):
            s_str = str(M[i][j])
            s_str = "".join((5 - len(s_str)) * [" "]) + s_str
            t_str += s_str + ", "
        t_str += "\n"
    print(t_str)


def print_succ(S):
    n = len(S)
    assert len(S) == len(S[0]), 'Dist mat not square'
    t_str = ""
    for i in range(n):
        for j in range(n):
            if S[i][j] is not None:
                t_str += f"{S[i][j]:3d}, "
            else:
                t_str += "  N, "
        t_str += "\n"
    print(t_str)
