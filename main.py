class main_app:
    import os

    class Installer:
        import os, shutil
        def __init__(self):
            self.Admin_Rights()

        def Admin_Rights(self):
            import os, sys, platform
            try:
                if str(platform.system()).lower().startswith('linux'):
                    open('/etc/Mod.txt', 'w+')
                    os.unlink('/etc/Mod.txt')
                elif str(platform.system()).lower().startswith('windows'):
                    os.mkdir(r'c:\Mod')
                    os.rmdir(r'c:\mod')
                else:
                    open('/etc/Mod.txt', 'w+')
                    os.unlink('/etc/Mod.txt')
                    try:
                        self.sys('chcp 65001')
                    except:
                        pass
                self.Import_Checker()
            except KeyboardInterrupt as e:
                self.os._exit(1)
            except Exception as e:
                e = e.args
                if e[0] == 13:
                    print('[+] Sorry You Need To Use Script As Admin Script Will Exit')
                    sys.exit(1)
                else:
                    pass

        def Import_Checker(self):
            try:
                __import__('imp').find_module('selenium')
            except ImportError:
                import pip
                pip.main(['install', 'selenium'])
                self.Import_Checker()
                pass
            except Exception as e:
                pass
            try:
                __import__('imp').find_module('requests')
            except ImportError:
                import pip
                pip.main(['install', 'requests'])
                self.Import_Checker()
                pass
            except Exception as e:
                pass
            try:
                __import__('imp').find_module('selenium')
            except ImportError:
                import pip
                pip.main(['install', 'selenium'])
                self.checker()
                pass
            except Exception as e:
                pass
            Auto_Bot.Facebook()

    class checker:
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        from selenium.common.exceptions import TimeoutException
        import warnings, os

        def __init__(self):
            print()
            self.warnings.simplefilter('ignore')
            self.browser = self.webdriver.PhantomJS(executable_path=r'c:\phantomjs.exe')
            list_path = input('[+]please enter list name: ')
            if self.os.path.isfile(list_path):
                accounts = open(list_path).readlines()
                print('[+]Starting')
                self.file = open('c1.txt', 'w+')
                for account in accounts:
                    print('[+]Checking %s' % account.strip())
                    self.main_checker(account.strip())
            else:
                print('[-]Will exit invalid accounts list path')
                self.os.exit(1)
            self.browser.quit()

        def main_checker(self, username):
            if username.casefold().endswith('@yahoo.com') or username.replace('+', '').replace('-', '').isnumeric():
                if not self.yahoo_checker(username):
                    if self.Facebook_checker(username):
                        print('[+]%s Can Be Exploited' % username)
                        self.file.write('%s\n' % username)
                    else:
                        print('[-]%s Is Free on Facebook and Yahoo' % username)
                        pass
                else:
                    print('[-]%s Cannot Be Exploited' % username)
                    pass
            else:
                print('[-]%s Is Free On Yahoo' % username)
                pass

        def yahoo_checker(self, username):
            self.browser.get(
                'https://login.yahoo.com/forgot?done=https%3A%2F%2Flogin.yahoo.com%2Faccount%2Fpersonalinfo')
            self.WebDriverWait(self.browser, 10).until(lambda x: x.find_element_by_name('verifyYid'))
            self.browser.find_element_by_id('username').send_keys(username)
            self.browser.find_element_by_name('verifyYid').send_keys(self.Keys.ENTER)
            try:
                self.WebDriverWait(self.browser, 10).until(lambda x: x.find_element_by_class_name('error-msg'))
                return False
            except self.TimeoutException:
                return True
            pass

        def Facebook_checker(self, username):
            self.browser.get('https://m.facebook.com/login/identify')
            self.WebDriverWait(self.browser, 10).until(lambda x: x.find_element_by_name('did_submit'))
            self.browser.find_element_by_name('email').send_keys(username)
            self.browser.find_element_by_name('did_submit').send_keys(self.Keys.ENTER)
            if self.browser.current_url.__contains__('search_attempts'):
                return False
            else:
                return True
            pass

    def __init__(self):
        try:
            self.Installer()
            def title():
                import os
                os.system(
                    'title TPCT Version 1' if os.name == 'nt' else
                    '\x1b]2;TPCT Version 1\x07')

            title()

            def cls():
                import os
                os.system('cls' if os.name == 'nt' else 'clear')

            cls()
            self.network_checker()
            self.Service_Start()
        except KeyboardInterrupt:
            self.os.exit()
        finally:
            pass
        pass

    def network_checker(self):
        import requests
        try:
            response = requests.get('https://m.facebook.com')
        except requests.exceptions.ConnectionError:
            print('[-] Network Is Not Connected. System will exit')
            self.os._exit(1)
        except:
            pass

    def Service_Start(self):
        title = """
 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || |   ______     | || |     ______   | || |  _________   | |
| | |  _   _  |  | || |  |_   __ \   | || |   .' ___  |  | || | |  _   _  |  | |
| | |_/ | | \_|  | || |    | |__) |  | || |  / .'   \_|  | || | |_/ | | \_|  | |
| |     | |      | || |    |  ___/   | || |  | |         | || |     | |      | |
| |    _| |_     | || |   _| |_      | || |  \ `.___.'\  | || |    _| |_     | |
| |   |_____|    | || |  |_____|     | || |   `._____.'  | || |   |_____|    | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' 
                            Th3 Professional Cod3r
Github: https://github.com/TPCT
Facebook: https://www.facebook.com/Taylor.Ackerley.9"""
        print(title)
        self.checker()
main_app()
