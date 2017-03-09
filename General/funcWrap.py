def main():
    """""
    Example usage:
    python funcWrap.py -f tests.api.test_convert.bin_to_frac --params {'num':0x55}
    This assumes a python file exits at tests/api/test_convert.py and the function
      bin_to_frac accepts 'num' as a argument
    """""

    from optparse import OptionParser
    from importlib import import_module
    import ast
    parser = OptionParser()
    
    # normal or one-off test options (wrapper replacement)
    parser.add_option("-f", "--func",
                      action="store", dest="func",
                      help="The name of the fully-referenced test function to execute. Ex: 'api.bx.test_version'. "
                           "You can also use linux dir separators: 'tests/api/bx/test_version'")
    parser.add_option("-p", "--params",
                      action="store", dest="params", default="{}",
                      help="The parameters to pass to the function specified with the 'func' option. Will be evaluated "
                           "as python, so it needs to be python compatible. Ex: --params {'die':0,'ip':0,'test':True}")
    
    (options, args) = parser.parse_args()
    
    if options.func:
        # running a single function
        # get the modules but not the test name at the end
        test_list = options.func.replace('/', '.')
        test_list = test_list.split('.')
        test_list = [x.strip() for x in test_list]
      
        mod_str = '.'.join(test_list[:-1])
        mod = import_module(mod_str)
    
        fn_ptr = getattr(mod, test_list[-1])
        options.params = options.params.replace(' ', '')
        fn_params = ast.literal_eval(options.params)
    
        r = fn_ptr(**fn_params)

        return r
    
if __name__ == '__main__':
    script_ret = main()
