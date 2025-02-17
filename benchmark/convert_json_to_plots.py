import os
from datetime import datetime
import subprocess
import json
import re as regular_expression
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import globals_pipeline as g

#
# Function to flatten nested JSON
#
def flatten_json(nested_json, parent_key='', sep='.'):
    items = []
    for k, v in nested_json.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

#
# Process all json files into one dataframe.
#

def convert_json_file_to_json_data(
    json_filename : str, 
    timestamp_day : int, 
    timestamp_yymmdd : int, 
    softwareversion : str, 
    precision : int, 
    method : str):

    filepath_json = os.path.join(g.JSON_DIR, json_filename)
    print(filepath_json)

    # Convert json to dataframe
    with open(filepath_json, 'r') as file:
        data = json.load(file)

    data = flatten_json(data)

    # Extend the json data with file parameters    
    data["timestamp_day"] = timestamp_day
    data["timestamp_yymmdd"] = timestamp_yymmdd
    data["softwareversion"] = softwareversion
    data["precision"] = precision
    data["method"] = method

    return data


def convert_all_json_files_to_dataframe():

    # Capture all files in the directory
    all_files = os.listdir(g.JSON_DIR)

    # Select only the sql files
    json_files = [file for file in all_files if file.endswith('.json')]

    # Remove something if needed
    json_files = [file for file in json_files if not file.startswith('2022', 0)]

    # Sort the files
    json_files = sorted(json_files)

    # Add every json file into a dataframe row
    first_file = True

    for file in json_files:

        print(f"Processing json file: {file}")
        
        words = file.split('_')
        timestamp_day = words[0]
        timestamp_yymmdd = words[1]
        softwareversion = words[2]
        precision = words[3]
        method = words[4]

        json_data = convert_json_file_to_json_data(file, timestamp_day, timestamp_yymmdd, softwareversion, precision, method)

        # Append new row to dataframe
        if first_file:
            df = pd.DataFrame([json_data])
            first_file = False
        else:
            df.loc[len(df)] = json_data

    return df

#
# Plot functions
#

def generate_time_nr_qubits_plots_for_all_benchmarks(df):

    # Get unigue benchmarks
    benchmarks = sorted(df['statistics.benchmark'].str.split('_').str[0].unique())
    print(f'Number of benchmarks = {len(benchmarks)}')

    # Generate unique colors for each benchmark using seaborn color palette
    palette = sns.color_palette('husl', len(benchmarks))

    # Plotting time and nr qubits
    plt.figure(figsize=(10,6))
    for i, benchmark in enumerate(benchmarks):
        
        # Filter data for the current benchmark
        df_benchmark = \
            df[
                (df['statistics.benchmark'].str.split('_').str[0] == benchmark) & 
                (df['precision'] == '64') & 
                (df['method'] == 'MTBDD')
            ]

        # Plot scatter points
        plt.scatter(
            df_benchmark['statistics.n_qubits'], 
            df_benchmark['statistics.simulation_time'], 
            color=palette[i], 
            label=benchmark, 
            alpha=0.7,  # Transparency for overlapping points
            edgecolors='k'  # Black edge for points
        )

    # Enhance plot
    plt.title('Simulation time vs. number of qubits MTBDD 64 bit')
    plt.xlabel('Number of qubits')
    plt.ylabel('Wall Time (s)')
    plt.grid(True)
    plt.legend(title='Benchmarks MQT', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small')

    # Set axis ranges and scales
    plt.xlim(0, 20)  # Linear scale between 0 and 20
    plt.yscale('log')  # Logarithmic scale for y-axis
    plt.ylim(0.001, 10000)  # Logarithmic range between 0.001 and 100
 
    # Adjust layout to fit legend
    plt.tight_layout()

    # Ensure output directory exists
    os.makedirs(g.PLOTS_DIR, exist_ok=True)
    plot_path = os.path.join(g.PLOTS_DIR, 'time_nr_qubits_scatter.pdf')
    plt.savefig(plot_path)
    print(f"Plot for time qubits created, saved at {plot_path}")
        
    # Clear the plot for reuse
    plt.clf()

    return

#
# Time against time plots
#

def generate_time_time_method_plots(df):

    # Plotting time and nr qubits
    df_x = (
        df[
            (df['precision'] == '64') & 
            (df['method'] == 'QMDDmax')
          ]
    )
    df_y = (
        df[
            (df['precision'] == '64') & 
            (df['method'] == 'MTBDD')
          ]
    )

    # Merge the two DataFrames on the column to compare
    merged_df = df_x.merge(df_y, on='statistics.benchmark', how='outer', indicator=True)

    # Identify unequal values
    unequal_values = merged_df[merged_df['_merge'] != 'both']

    # Display the unequal values
    if not(unequal_values.empty):
        print("Unequal amount of rows in time time method plot:")
        print(unequal_values)

    # Plots drawing
    fig, ax = plt.subplots()

    ax.scatter(
        sorted(df_x['statistics.simulation_time']), 
        sorted(df_y['statistics.simulation_time']), 
        color='blue',
        marker='o'
        )

    # Set logarithmic scale for both axes
    ax.set_xscale('log')
    ax.set_yscale('log')

    # Set limits for both axes
    ax.set_xlim(0.0001, 100)
    ax.set_ylim(0.001, 10000)

    # Display the plot
    plt.title('Wall time of all benchmarks, precision=64')
    plt.xlabel('EVDD wall time (s)')
    plt.ylabel('MTBDD wall time (s)')
    plt.grid(True)

   # Ensure the output directory exists
    os.makedirs(g.PLOTS_DIR, exist_ok=True)
    plt.savefig(g.PLOTS_DIR + f'/time_time_method_sorted.pdf')

    print("Plot for time time method created")

    return

#
# Time against time plots
#

def generate_time_time_method_plots_for_all_benchmarks(df):

    # Get unique benchmarks
    benchmarks = sorted(df['statistics.benchmark'].str.split('_').str[0].unique())
    print(f'Number of benchmarks = {len(benchmarks)}')

    # Generate unique colors for each benchmark using seaborn color palette
    palette = sns.color_palette('husl', len(benchmarks))

    # Plotting time and nr qubits
    plt.figure(figsize=(10,6))
    for i, benchmark in enumerate(benchmarks):
        
        # Filter data for the current benchmark
        df_benchmark_x = \
            df[
                (df['statistics.benchmark'].str.split('_').str[0] == benchmark) & 
                (df['precision'] == '64') & 
                (df['method'] == 'MTBDD') &
                (df['statistics.workers'].astype(str) == '1')
            ]

        # Filter data for the current benchmark
        df_benchmark_y = \
            df[
                (df['statistics.benchmark'].str.split('_').str[0] == benchmark) & 
                (df['precision'] == '64') & 
                (df['method'] == 'MTBDD') &
                (df['statistics.workers'].astype(str) == '10')
            ]

        # Plot scatter points
        plt.scatter(
            sorted(df_benchmark_x['statistics.simulation_time']), 
            sorted(df_benchmark_y['statistics.simulation_time']), 
            color=palette[i], 
            label=benchmark, 
            alpha=0.7,  # Transparency for overlapping points
            edgecolors='k'  # Black edge for points
        )

    # Enhance plot
    plt.title('Wall times MTBDD workers=1 and 10, precision 64 bit')
    plt.xlabel('Wall time (s) MTBDD workers= 1')
    plt.ylabel('Wall time (s) MTBDD workers= 10')
    plt.grid(True)
    plt.legend(title='Benchmarks MQT', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small')

    # Set axis ranges and scales
    plt.xscale('log')  # Logarithmic scale for x-axis
    plt.xlim(0.001, 10000)  
    plt.yscale('log')  # Logarithmic scale for y-axis
    plt.ylim(0.001, 10000)  
 
    # Adjust layout to fit legend
    plt.tight_layout()

    # Ensure output directory exists
    os.makedirs(g.PLOTS_DIR, exist_ok=True)
    plot_path = os.path.join(g.PLOTS_DIR, 'time_time_scatter_sorted_MTBDD_1_10_Sylvan.pdf')
    plt.savefig(plot_path)
    print(f"Plot for time time created, saved at {plot_path}")
        
    # Clear the plot for reuse
    plt.clf()

    return

#
# Time against time plots
#

def generate_time_time_per_node_plots(df):

    # Plotting time and nr qubits
    df_x = (
        df[
            (df['precision'] == '64') & 
            (df['method'] == 'QMDDmax')
          ]
    )
    df_x = df_x.assign(time_per_node = df_x['statistics.simulation_time'] / df_x['statistics.final_nodes'])

    df_y = (
        df[
            (df['precision'] == '64') & 
            (df['method'] == 'MTBDD')
          ]
    )
    df_y = df_y.assign(time_per_node = df_y['statistics.simulation_time'] / df_y['statistics.final_nodes'])

    # Merge the two DataFrames on the column to compare
    merged_df = df_x.merge(df_y, on='statistics.benchmark', how='outer', indicator=True)

    # Identify unequal values
    unequal_values = merged_df[merged_df['_merge'] != 'both']

    # Display if there are unequal values
    if not(unequal_values.empty):
        print("Unequal values time time method per node:")
        print(unequal_values)

    # Plots drawing
    fig, ax = plt.subplots()

    ax.scatter(
        df_x['time_per_node'], 
        df_y['time_per_node'], 
        color='blue',
        marker='o'
        )

    # Set logarithmic scale for both axes
    ax.set_xscale('log')
    ax.set_yscale('log')

    # Set limits for both axes
    ax.set_xlim(0.00001, 1)
    ax.set_ylim(0.00001, 1)

    # Display the plot
    plt.title('Wall time per node of all benchmarks, precision=64')
    plt.xlabel('QMDD wall time (s)')
    plt.ylabel('MTBDD wall time (s)')
    plt.grid(True)

   # Ensure the output directory exists
    os.makedirs(g.PLOTS_DIR, exist_ok=True)
    plt.savefig(g.PLOTS_DIR + f'/time_time_per_node.pdf')

    print("Plot for time time methode per node created")

    return

#
# Time against time for different precisions plots
#

def generate_time_time_precision_plots(df):

    # Plotting time and nr qubits
    df_x = (
        df[
            (df['precision'] == '256') & 
            (df['method'] == 'MTBDD')
          ]
    )
    df_y = (
        df[
            (df['precision'] == '64') & 
            (df['method'] == 'MTBDD')
          ]
    )

    # Merge the two DataFrames on the column to compare
    merged_df = df_x.merge(df_y, on='statistics.benchmark', how='outer', indicator=True)

    # Identify unequal values
    unequal_values = merged_df[merged_df['_merge'] != 'both']

    # Display the unequal values
    if not(unequal_values.empty):
        print("Unequal values time time precision:")
        print(unequal_values)

    # Plots drawing
    fig, ax = plt.subplots()

    ax.scatter(
        df_x['statistics.simulation_time'], 
        df_y['statistics.simulation_time'], 
        color='blue',
        marker='o'
        )

    # Set logarithmic scale for both axes
    ax.set_xscale('log')
    ax.set_yscale('log')

    # Set limits for both axes
    ax.set_xlim(0.001, 100)
    ax.set_ylim(0.001, 100)

    # Display the plot
    plt.title('Wall time of all benchmarks, precision 64 against 256')
    plt.xlabel('MTBDD 256 wall time (s)')
    plt.ylabel('MTBDD 64 wall time (s)')
    plt.grid(True)

   # Ensure the output directory exists
    os.makedirs(g.PLOTS_DIR, exist_ok=True)
    plt.savefig(g.PLOTS_DIR + f'/time_time_precision.pdf')

    print("Plot for time time precision created")

    return

#
# Norm of state vector against norm for different method plots
#

def generate_norm_norm_method_plots(df):

    # Plotting norms
    df_x = (
        df[
            (df['precision'] == '64') & 
            (df['method'] == 'MTBDD')
          ]
    )
    df_y = (
        df[
            (df['precision'] == '64') & 
            (df['method'] == 'QMDDmax')
          ]
    )

    # Merge the two DataFrames on the column to compare
    merged_df = df_x.merge(df_y, on='statistics.benchmark', how='outer', indicator=True)

    # Identify unequal values
    unequal_values = merged_df[merged_df['_merge'] != 'both']

    # Display the unequal values
    if not(unequal_values.empty):
        print("Unequal values norm norm method:")
        print(unequal_values)

    # Plots drawing
    fig, ax = plt.subplots()

    ax.scatter(
        df_x['statistics.norm'], 
        df_y['statistics.norm'], 
        color='blue',
        marker='o'
        )

    # Set logarithmic scale for both axes
    ax.set_xscale('linear')
    ax.set_yscale('linear')

    # Set limits for both axes
    # ax.set_xlim(0.1, 1)
    # ax.set_ylim(0.1, 1)

    # Display the plot
    plt.title('Norm state vector of all benchmarks, precision 64')
    plt.xlabel('MTBDD 64 norm')
    plt.ylabel('QMDD 64 norm')
    plt.grid(True)

   # Ensure the output directory exists
    os.makedirs(g.PLOTS_DIR, exist_ok=True)
    plt.savefig(g.PLOTS_DIR + f'/norm_norm_method.pdf')

    print("Plot for norm norm method created")

    return

#
# Norm of state vector against norm for different precision plots
#

def generate_norm_norm_precision_plots(df):

    # Plotting norms
    df_x = (
        df[
            (df['precision'] == '64') & 
            (df['method'] == 'MTBDD')
          ]
    )
    df_y = (
        df[
            (df['precision'] == '16') & 
            (df['method'] == 'MTBDD')
          ]
    )

    # Merge the two DataFrames on the column to compare
    merged_df = df_x.merge(df_y, on='statistics.benchmark', how='outer', indicator=True)

    # Identify unequal values
    unequal_values = merged_df[merged_df['_merge'] != 'both']

    # Display the unequal values
    if not(unequal_values.empty):
        print("Unequal values norm norm precision:")
        print(unequal_values)

    # Plots drawing
    fig, ax = plt.subplots()

    ax.scatter(
        df_x['statistics.norm'], 
        df_y['statistics.norm'], 
        color='blue',
        marker='o'
        )

    # Set logarithmic scale for both axes
    ax.set_xscale('linear')
    ax.set_yscale('linear')

    # Set limits for both axes
    ax.set_xlim(0.999, 1.001)
    ax.set_ylim(0.999, 1.001)

    # Display the plot
    plt.title('Norm state vector of all benchmarks, method MTBDD')
    plt.xlabel('MTBDD 64 norm')
    plt.ylabel('MTBDD 16 norm')
    plt.grid(True)

   # Ensure the output directory exists
    os.makedirs(g.PLOTS_DIR, exist_ok=True)
    plt.savefig(g.PLOTS_DIR + f'/norm_norm_precision.pdf')

    print("Plot for norm norm precision created")

    return

#
# Time and number of qubits plot
#

def generate_time_nr_qubits_plots_for_random(df):

    # Filter x and y axes
    df_x = (
        df[
            (df['precision'] == f'{g.PRECISION}') & 
            (df['method'] == f'{g.METHOD}')
          ]
    )
    df_y = (
        df[
            (df['precision'] == f'{g.PRECISION}') & 
            (df['method'] == f'{g.METHOD}')
          ]
    )

    # Merge the two DataFrames on the column to compare
    merged_df = df_x.merge(df_y, on='statistics.benchmark', how='outer', indicator=True)

    # Identify unequal values
    unequal_values = merged_df[merged_df['_merge'] != 'both']

    # Display the unequal values
    if not(unequal_values.empty):
        print("Unequal values time nr qubits:")
        print(unequal_values)

    # Plots drawing
    fig, ax = plt.subplots()

    ax.scatter(
        df_x['statistics.n_qubits'], 
        df_y['statistics.simulation_time'], 
        color='blue',
        marker='o'
        )

    # Set logarithmic scale for both axes
    ax.set_xscale('linear')
    ax.set_yscale('log')

    # Set limits for both axes
    ax.set_xlim(0, g.MAX_NUM_QUBITS)
    ax.set_ylim(0.001, 10.0)

    # Display the plot
    plt.title(f'Clifford + T, {g.PERCENTAGE_T_GATES} percent random T, {g.NUM_CIRCUITS}x, {g.MIN_NUM_QUBITS}-{g.MAX_NUM_QUBITS}({g.STEPSIZE_NUM_QUBITS}), {g.MIN_NUM_GATES}-{g.MAX_NUM_GATES}({g.STEPSIZE_NUM_GATES})')
    plt.xlabel(f'{g.METHOD} number qubits')
    plt.ylabel(f'{g.METHOD} time(seconds)')
    plt.grid(True)

   # Ensure the output directory exists
    os.makedirs(g.PLOTS_DIR, exist_ok=True)

    plt.savefig(g.PLOTS_DIR + f'/time_nr_qubits_{g.PERCENTAGE_T_GATES}_percent_{g.MIN_NUM_QUBITS}_{g.MAX_NUM_QUBITS}_{g.MIN_NUM_GATES}_{g.MAX_NUM_GATES}.pdf')

    print("Plot for time nr_qubits created")

    return
