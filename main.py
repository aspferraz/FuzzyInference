from output.fuzzy_variable_output import FuzzyOutputVariable
from input.fuzzy_variable_input import FuzzyInputVariable
from controller.fuzzy_system import FuzzySystem


def configure_variables(fuzzy_system):
    # inputs
    temperature = FuzzyInputVariable('Temperature', 800, 1200, 500)
    temperature.add_trapezoidal('Low', 800, 800, 900, 1000)
    temperature.add_triangular('Medium', 900, 1000, 1100)
    temperature.add_trapezoidal('High', 1000, 1100, 1200, 1200)

    volume = FuzzyInputVariable('Volume', 2, 12, 500)
    volume.add_trapezoidal('Small', 2, 2, 4.5, 7)
    volume.add_triangular('Medium', 4.5, 7, 9.5)
    volume.add_trapezoidal('Large', 7, 9.5, 12, 12)

    # output
    pressure = FuzzyOutputVariable('Pressure', 4, 12, 500)
    pressure.add_trapezoidal('Low', 4, 4, 5, 8)
    pressure.add_triangular('Medium', 6, 8, 10)
    pressure.add_trapezoidal('High', 8, 11, 12, 12)

    fuzzy_system.add_input_variable(temperature)
    fuzzy_system.add_input_variable(volume)
    fuzzy_system.add_output_variable(pressure)


def configure_rules(fuzzy_system):
    fuzzy_system.add_rule({'Temperature': 'Low', 'Volume': 'Small'}, {'Pressure': 'Low'})
    fuzzy_system.add_rule({'Temperature': 'Medium', 'Volume': 'Small'}, {'Pressure': 'Low'})
    fuzzy_system.add_rule({'Temperature': 'High', 'Volume': 'Small'}, {'Pressure': 'Medium'})
    fuzzy_system.add_rule({'Temperature': 'Low', 'Volume': 'Medium'}, {'Pressure': 'Low'})
    fuzzy_system.add_rule({'Temperature': 'Medium', 'Volume': 'Medium'}, {'Pressure': 'Medium'})
    fuzzy_system.add_rule({'Temperature': 'High', 'Volume': 'Medium'}, {'Pressure': 'High'})
    fuzzy_system.add_rule({'Temperature': 'Low', 'Volume': 'Large'}, {'Pressure': 'Medium'})
    fuzzy_system.add_rule({'Temperature': 'Medium', 'Volume': 'Large'}, {'Pressure': 'High'})
    fuzzy_system.add_rule({'Temperature': 'High', 'Volume': 'Large'}, {'Pressure': 'High'})


def run():
    sys = FuzzySystem()
    configure_variables(sys)
    configure_rules(sys)

    inputs_list = [
        {'Temperature': 965, 'Volume': 11},
        {'Temperature': 920, 'Volume': 7.6},
        {'Temperature': 1050, 'Volume': 6.3},
        {'Temperature': 843, 'Volume': 8.6},
        {'Temperature': 1122, 'Volume': 5.2}
    ]
    for inputs in inputs_list:
        output = sys.evaluate_output(inputs)
        print(inputs, output)

    sys.plot_system()


if __name__ == '__main__':
    run()
