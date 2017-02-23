from optparse import OptionParser
parser = OptionParser()

# normal or one-off test options (wrapper replacement)
parser.add_option("-f", "--func",
                  action="store", dest="func",
                  help="The name of the fully-referenced test function to execute. Ex: 'api.bx.test_version'. "
                       "You can also use linux dir separators: 't/a/b/test_version'")
parser.add_option("--params",
                  action="store", dest="params", default="{}",
                  help="The parameters to pass to the function specified with the 'func' option. Will be evaluated "
                       "as python, so it needs to be python compatible. Ex: '(16, range(0x10), debug=True)'")

# options for running groups or suites
parser.add_option("-t", "--test",
                  action="store", dest="test",
                  help="Run a test from within the desired suites, must specify suites option.")
parser.add_option("-g", "--group",
                  action="store", dest="group", default=None,
                  help="Run a suite/group of tests within the desired suites, must specify suites option.")
parser.add_option("-l", "--list_tests",
                  action="store_true", dest="list_tests",
                  help="List the available tests but don't run anything")

# common options
parser.add_option("-n", "--number_iterations",
                  action="store", dest="number_iterations", default="-1",
                  help="The number of iterations of the test to run")
parser.add_option("-e", "--halt_on_first_error",
                  action="store_true", dest="halt_on_first_error", default=False,
                  help="Halt the regression after the first failure for debugging purposes")

# default target to use (not normally used, only for functions that don't already specify one)
parser.add_option("-i", "--ip",
                  action="store", dest="ip",
                  help="The remote IP to communicate with, only used if the test doesn't specify directly")
parser.add_option("-p", "--port",
                  action="store", dest="port", default=50000,
                  help="The remote port to communicate with, only used if the test doesn't specify directly")
parser.add_option("-a", "--api",
                  action="store", dest="api",
                  help="The API to use against this target, either ax or bx")

# Advanced and/or jenkins options
parser.add_option("-b", "--buffer_writes",
                  action="store_true", dest="buffer_writes",
                  help="Save writes to a buffer and push them to the device as a single block. "
                       "Don't use this unless you know what you're doing.")
parser.add_option("--test_table",
                  action="store", dest="test_table",
                  help="Generate a big table of which rules were tested with what other rules (for jenkins) "
                       "and output them to this filename")
parser.add_option("-r", "--report",
                  action="store", dest="report",
                  help="Generate a report file describing the test suite (for jenkins)")
parser.add_option("-x", "--xml",
                  action="store", dest="xml",
                  help="Generate an XML file with the test results (for jenkins)")
parser.add_option("--seed",
                  action="store", dest="seed",
                  help="The seed to use to reproduce a test (for jenkins)")
parser.add_option("--build_number",
                  action="store", dest="build_number",
                  help="The build number generated by the Jenkins regression server")
(options, args) = parser.parse_args()


print options

if options.build_number:
    print "Your build number is", options.build_number
else:
    # the default
    pass

print "buffer writes is TRUE" if options.buffer_writes else "buffer writes is FALSE"

rx_fifo = range(0, 10)
tx_fifo = [11, 12, 13]

print rx_fifo
val_rx = rx_fifo.pop(0)
val_tx = tx_fifo.pop(0)
print rx_fifo
print val_rx
print val_tx
