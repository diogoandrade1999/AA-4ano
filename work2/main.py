import argparse
import random
import math

from Counter import Counter


def write_results(counter:Counter, counters:dict, trials:int) -> None:
    """Write the counter results on file"""

    with open('output_' + str(len(counter.chain)) + '_' + str(trials) + '.txt', 'w') as target:
        target.write('Chain size %d – %d trials\n' % (len(counter.chain), trials))
        target.write('Chain: %s\n' % counter.chain)

        for letter in counter.exact_count.keys():
            target.write('\nLetter: %s\n' % letter)

            target.write('\tExact value: %d\n' % counter.exact_count[letter])

            for name, data in counters.items():
                counts:str = data[0]
                calculations:dict = data[1]

                target.write('\n\t%s Counter:\n' % name)
                
                for calculation_name, calculation in calculations[letter].items():
                    if calculation is None:
                        target.write('\n')
                    else:
                        target.write('\t\t%s: %s\n' % (calculation_name, calculation))

                if letter in counts:
                    target.write('\n')
                    for count, times in sorted(counts[letter].items(), key=lambda item: item[0]):
                        target.write('\t\tcounter value: %10d - %10d times\n' % (count, times))


def print_results(counter:Counter, counters:dict, trials:int) -> None:
    """Print the counter results"""

    print('Chain size %d – %d trials' % (len(counter.chain), trials))
    print('Chain: %s' % counter.chain)

    for letter in counter.exact_count.keys():
        print('\nLetter: %s' % letter)

        print('\tExact value: %d' % counter.exact_count[letter])

        for name, data in counters.items():
            counts:str = data[0]
            calculations:dict = data[1]

            print('\n\t%s Counter:' % name)
            
            for calculation_name, calculation in calculations[letter].items():
                if calculation is None:
                    print()
                else:
                    print('\t\t%s: %s' % (calculation_name, calculation))

            if letter in counts:
                print()
                for count, times in sorted(counts[letter].items(), key=lambda item: item[0]):
                    print('\t\tcounter value: %10d - %10d times' % (count, times))


def calculations(exact_counter:dict, other_counter:dict, prob:float=None, base_log:float=None) -> dict:
    """Calcule the errors, mean, ... for the Counters"""
    errors:dict = {}
    for letter, exact_count in exact_counter.items():
        other_counts:list = [0]
        if letter in other_counter:
            for value, repetitions in other_counter[letter].items():
                for _ in range(repetitions):
                    other_counts += [value]

        expected_value:float = 0
        expected_variance:float = 0
        expected_standard_deviation:float = 0
        if prob:
            expected_value:float = math.floor(round(exact_count * prob))
            expected_variance:float = exact_count * prob * (1 - prob)
            expected_standard_deviation:float = math.sqrt(expected_variance)
        elif base_log:
            expected_value:float = math.floor(math.log(exact_count + 1, base_log))
            prob:float = 1 / base_log
            expected_variance:float = exact_count * prob * (1 - prob)
            expected_standard_deviation:float = math.sqrt(expected_variance)

        absolute_error:list = [abs(count  - expected_value) for count in other_counts]
        max_absolute_error:int = max(absolute_error)
        min_absolute_error:int = min(absolute_error)
        mean_absolute_error:float = sum(absolute_error) / len(absolute_error)

        relative_error:list = [2 * (abs(count  - expected_value) / (count + expected_value)) for count in other_counts if (count + expected_value) > 0]
        max_relative_error:float = max(relative_error) * 100
        min_relative_error:float = min(relative_error) * 100
        mean_relative_error:float = sum(relative_error) / len(relative_error) * 100

        largest_counter_value:int = max(other_counts)
        smaller_counter_value:int = min(other_counts)

        mean:float = sum(other_counts) / len(other_counts)
        deviation:list = [abs(count - mean) for count in other_counts]
        max_deviation:float = max(deviation)
        mean_absolute_deviation:float = sum(deviation) / len(deviation)
        variance:float = sum([d ** 2 for d in deviation]) / len(other_counts)
        standard_deviation:float = math.sqrt(variance)

        errors[letter]:dict = {
            "Expected Value": str(expected_value),
            "Expected Variance": str(round(expected_variance, 2)),
            "Expected Standard Deviation": str(round(expected_standard_deviation, 2)),
            "1": None,
            "Max Absolute Error": str(round(max_absolute_error, 2)),
            "Min Absolute Error": str(round(min_absolute_error, 2)),
            "Mean Absolute Error": str(round(mean_absolute_error, 2)),
            "2": None,
            "Max Relative Error": str(round(max_relative_error, 2)) + '%',
            "Min Relative Error": str(round(min_relative_error, 2)) + '%',
            "Mean Relative Error": str(round(mean_relative_error, 2)) + '%',
            "3": None,
            "Largest Counter Value": str(largest_counter_value),
            "Smaller Counter Value": str(smaller_counter_value),
            "4": None,
            "Mean Counter Value": str(round(mean, 2)),
            "Mean Absolute Deviation": str(round(mean_absolute_deviation, 2)),
            "Standard Deviation": str(round(standard_deviation, 2)),
            "Maximum Deviation": str(round(max_deviation, 2)),
            "Variance": str(round(variance, 2)),
        }
    return errors


def update_counter(counts:dict, counters:dict) -> dict:
    """Update the counter results"""
    for letter in counts.keys():
        count:int = counts[letter]
        counters[letter]:dict = counters.get(letter, {})
        counters[letter][count]:int = counters[letter].get(count, 0) + 1
    return counters


def create_chain(alphabet:str, size:int) -> str:
    """Create the chain"""
    return ''.join(random.choice(alphabet) for i in range(size))


def run(alphabet:str, chain_size:int, trials:int, prob:float, base_log:float, show_result:bool) -> None:
    """Run the tests"""
    # * Create the chain
    chain:str = create_chain(alphabet, chain_size)

    # * Create the Counter
    counter:Counter = Counter(chain, prob, base_log)

    # * Save the Counter results
    prob_counters:dict = {}
    log_counters:dict = {}

    # * Test multiple times
    for i in range(trials):
        # * Update the result counters
        prob_counters:dict = update_counter(counter.prob_counter(), prob_counters)
        log_counters:dict = update_counter(counter.log_counter(), log_counters)

    # * Calcule the errors for the Prob and Log Counters
    prob_errors = calculations(counter.exact_count, prob_counters, prob=prob)
    log_errors = calculations(counter.exact_count, log_counters, base_log=base_log)

    # * Print or write the results of the counters
    if show_result:
        print_results(
            counter=counter,
            counters={
                    "Prob 1/16": (prob_counters, prob_errors),
                    "Log with base sqtr(2)": (log_counters, log_errors)
                },
            trials=trials
        )
    else:
        write_results(
            counter=counter,
            counters={
                    "Prob 1/16": (prob_counters, prob_errors),
                    "Log with base sqtr(2)": (log_counters, log_errors)
                },
            trials=trials
        )
        print('Look the file: output_' + str(chain_size) + '_' + str(trials) + '.txt')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", dest="alphabet", required=False, help="Chain characters, default='diogoandrélopesandrade'", type=str, default="diogoandrélopesandrade")
    parser.add_argument("-s", dest="chain_size", required=False, help="Chain size, default=100", type=int, default=100)
    parser.add_argument("-t", dest="trials", required=False, help="Number of test repetitions, default=1000", type=int, default=1000)
    parser.add_argument("-p", dest="prob", required=False, help="Probability of counter, default=1/16", type=float, default=1/16)
    parser.add_argument("-b", dest="base_log", required=False, help="Base of logarithm of counter, default=sqrt(2)", type=float, default=math.sqrt(2))
    parser.add_argument("-w", dest="show_results", required=False, help="Show Results, default: Write on file", default=False, action='store_true')
    args = parser.parse_args()

    run(alphabet=args.alphabet,
        chain_size=args.chain_size,
        trials=args.trials,
        prob=args.prob,
        base_log=args.base_log,
        show_result=args.show_results)
