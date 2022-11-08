from datetime import datetime

output_file = "experiments/bench_{}.sh"
csv_output  = "experiments/bench_{}_res.csv"

run_grov = "timeout {} ./build/examples/alg_run grover --qubits={} --norm-strat={} --tol={} --workers={} --csv-output={}\n"
run_shor = "timeout {} ./build/examples/alg_run shor --shor-N={} --norm-strat={} --tol={} --workers={} --csv-output={}\n"
run_sup  = "timeout {} ./build/examples/alg_run supremacy --qubits={} --depth={} --norm-strat={} --tol={} --workers={} --csv-output={}\n"


def init_output_file():
    global output_file
    global csv_output
    dt_string = datetime.now().strftime("%Y%m%d%m_%H%M%S")
    output_file = output_file.format(dt_string)
    csv_output  = csv_output.format(dt_string)
    print(f"writing to {output_file}")

    with open(output_file, 'w') as f:
        f.write("#!/bin/bash\n\n")


def experiments_grover():

    # configs to test
    timeout = '10m'
    qubits = [5,7,9]
    tol = [1e-14]
    norm_strat = ['low', 'largest', 'l2']
    workers = [1,2]

    with open(output_file, 'a') as f:
        f.write("# grover experiments\n")
        for q in qubits:
            for ns in norm_strat:
                for t in tol:
                    for w in workers:
                        f.write(run_grov.format(timeout, q, ns, t, w, csv_output))
        f.write("\n")


def experiments_shor():

    # configs to test
    timeout = '10m'
    shor_N = [15,40]
    tol = [1e-14]
    norm_strat = ['largest']
    workers = [1,2]

    with open(output_file, 'a') as f:
        f.write("# shor experiments\n")
        for N in shor_N:
            for ns in norm_strat:
                for t in tol:
                    for w in workers:
                        f.write(run_shor.format(timeout, N, ns, t, w, csv_output))
        f.write("\n")

def experiments_supremacy():

    # configs to test
    timeout = '10m'
    qubits = [20]
    depth = [5,6,7]
    tol = [1e-14]
    norm_strat = ['largest']
    workers = [1,2]

    with open(output_file, 'a') as f:
        f.write("# supremacy experiments\n")
        for q in qubits:
            for d in depth:
                for ns in norm_strat:
                    for t in tol:
                        for w in workers:
                            f.write(run_sup.format(timeout, q, d, ns, t, w, csv_output))
        f.write("\n")


if __name__ == '__main__':
    init_output_file()
    experiments_grover()
    experiments_shor()
    experiments_supremacy()