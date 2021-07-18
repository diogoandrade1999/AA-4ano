import argparse
import math

from pprint import pprint

from Counter import Counter
from main import create_chain, update_counter, calculations


def data(values:dict) -> dict:
    expected_value:list = []
    expected_variance:list = []
    expected_standard_deviation:list = []
    max_absolute_error:list = []
    min_absolute_error:list = []
    mean_absolute_error:list = []
    max_relative_error:list = []
    min_relative_error:list = []
    mean_relative_error:list = []
    mean:list = []
    mean_absolute_deviation:list = []
    standard_deviation:list = []
    max_deviation:list = []
    variance:list = []
    for letter, value in values.items():
        expected_value += [int(value["Expected Value"])]
        expected_variance += [float(value["Expected Variance"])]
        expected_standard_deviation += [float(value["Expected Standard Deviation"])]
        max_absolute_error += [float(value["Max Absolute Error"])]
        min_absolute_error += [float(value["Min Absolute Error"])]
        mean_absolute_error += [float(value["Mean Absolute Error"])]
        max_relative_error += [float(value["Max Relative Error"][:-1])]
        min_relative_error += [float(value["Min Relative Error"][:-1])]
        mean_relative_error += [float(value["Mean Relative Error"][:-1])]
        mean += [float(value["Mean Counter Value"])]
        mean_absolute_deviation += [float(value["Mean Absolute Deviation"])]
        standard_deviation += [float(value["Standard Deviation"])]
        max_deviation += [float(value["Maximum Deviation"])]
        variance += [float(value["Variance"])]

    expected_value = sum(expected_value)
    expected_variance = sum(expected_variance) / len(expected_variance)
    expected_standard_deviation = sum(expected_standard_deviation) / len(expected_standard_deviation)
    max_absolute_error = sum(max_absolute_error) / len(max_absolute_error)
    min_absolute_error = sum(min_absolute_error) / len(min_absolute_error)
    mean_absolute_error = sum(mean_absolute_error) / len(mean_absolute_error)
    max_relative_error = sum(max_relative_error) / len(max_relative_error)
    min_relative_error = sum(min_relative_error) / len(min_relative_error)
    mean_relative_error = sum(mean_relative_error) / len(mean_relative_error)
    mean = sum(mean) / len(mean)
    mean_absolute_deviation = sum(mean_absolute_deviation) / len(mean_absolute_deviation)
    standard_deviation = sum(standard_deviation) / len(standard_deviation)
    max_deviation = sum(max_deviation) / len(max_deviation)
    variance = sum(variance) / len(variance)

    result:dict = {
        "Expected Value": str(expected_value),
        "Expected Variance": str(round(expected_variance, 2)),
        "Expected Standard Deviation": str(round(expected_standard_deviation, 2)),
        "Max Absolute Error": str(round(max_absolute_error, 2)),
        "Min Absolute Error": str(round(min_absolute_error, 2)),
        "Mean Absolute Error": str(round(mean_absolute_error, 2)),
        "Max Relative Error": str(round(max_relative_error, 2)) + '%',
        "Min Relative Error": str(round(min_relative_error, 2)) + '%',
        "Mean Relative Error": str(round(mean_relative_error, 2)) + '%',
        "Mean Counter Value": str(round(mean, 2)),
        "Mean Absolute Deviation": str(round(mean_absolute_deviation, 2)),
        "Standard Deviation": str(round(standard_deviation, 2)),
        "Maximum Deviation": str(round(max_deviation, 2)),
        "Variance": str(round(variance, 2)),
    }
    return result


def test(alphabet:str, chain_size:int, trials:int, prob:float, base_log:float) -> None:
    """Run the tests"""
    # * Save the Counter results
    prob_counters:dict = {}
    log_counters:dict = {}

    # * Create the chain
    chain = create_chain(alphabet, chain_size)

    # * Create the Counter
    counter = Counter(chain, prob, base_log)

    # * Test multiple times
    for i in range(trials):
        # * Update the result counters
        prob_counters = update_counter(counter.prob_counter(), prob_counters)
        log_counters = update_counter(counter.log_counter(), log_counters)

    # * Calcule the errors for the Prob and Log Counters
    prob_errors = calculations(counter.exact_count, prob_counters, prob=prob)
    log_errors = calculations(counter.exact_count, log_counters, base_log=base_log)

    # * Print the results of the counters
    print('Chain size %d – %d trials' % (len(chain), trials))
    print()
    print('Prob 1/16 Counter:')
    pprint(data(prob_errors))
    print()
    print('Log with base sqtr(2) Counter:')
    pprint(data(log_errors))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", dest="alphabet", required=False, help="Chain characters, default='diogoandrélopesandrade'", type=str, default="diogoandrélopesandrade")
    parser.add_argument("-s", dest="chain_size", required=False, help="Chain size, default=100", type=int, default=100)
    parser.add_argument("-t", dest="trials", required=False, help="Number of test repetitions, default=1000", type=int, default=1000)
    parser.add_argument("-p", dest="prob", required=False, help="Probability of counter, default=1/16", type=float, default=1/16)
    parser.add_argument("-b", dest="base_log", required=False, help="Base of logarithm of counter, default=sqrt(2)", type=float, default=math.sqrt(2))
    args = parser.parse_args()

    test(alphabet=args.alphabet,
        chain_size=args.chain_size,
        trials=args.trials,
        prob=args.prob,
        base_log=args.base_log)
