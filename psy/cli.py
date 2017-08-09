"""Python packaging facility for lambda function...

Usage:
  psy list
  psy (-h | --help)

Options:
  -h --help     Show this screen.

"""

from docopt import docopt

def main():
    arguments = docopt(__doc__, version='0.1.0')
    print(arguments)

if __name__ == '__main__':
    main()

#
# step 1. Create a real python package for your aws lambda function, with setup.py etc.
#         Now your lambda handler is somewhere within your modules, let say 'ecstasks.main:register_task'.
#
#         Add you lambda handler as an entry point for your package under the name ```psy.lambda_handler```
#         ex in a setup.cfg it will look like:
#
#     ```...
#         [entry_points]
#         psy.lambda_handler =
#             main = ecstasks.main:register_task ```
#
#         >> Nothing really unusual, and check you can build your package with:
#
#     ``` $ python setup.py sdist ```
#
# step 2. Install psy
#
#     ``` $ pip install psy```
#
#         >> This will add a task to your setup.py called ```bdist_lambda``` you can check it on the setup.py help.
#
# step 3. Generate the lambda package with all the dependencies:
#
#     ``` $ python setup.py bdist_lambda```
#
#         >> Now this create your self contained aws lambda zip file, with all your project dependecy installed
#         under ```build``` directory. Your can upload that file as a aws lambda, and
#
#         >> Bonus points:
#             * The name of your lambda handler is the name you gave to your entry point in setup.cfg
#              i.e (for here): main.
#             * You can have more than one handler in one packages, you will have one zip file and depending on which
#               name you use in lambda configuration, the right handler will be used.
#             * The generated zip file is actually an executable file (a pex format) and executing it
#               will drop you in a python REPL with your environment loaded.



#
#
# class ListHandler(Lister):
#     """List Python package with declared lambda_handler entry point."""
#     log = logging.getLogger(__name__)
#
#     def get_parser(self, prog_name):
#         parser = super(ListHandler, self).get_parser(prog_name)
#         # add limits.
#         return parser
#
#     def take_action(self, parsed_args):
#         return
#
#
# def main(argv=sys.argv[1:]):
#     app = PsyCLI()
#     return app.run(argv)
#
#
# if __name__ == '__main__':
#     sys.exit(main(sys.argv[1:]))
