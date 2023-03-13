import mechanize
class link_generator:
    def __init__(self,model_id):
        br = mechanize.Browser()
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        br.open("https://turbo.az")
        br.select_form(name="q_form")
        br.find_control(name='q[model][]',nr=1).get('{}'.format(model_id)).selected=True
        #br.find_control(name='q[make][]').get('{}'.format(marka_id)).selected=True
        # br.find_control(name='q[color][]',nr=1).get('{}'.format('')).selected=True
        # br.find_control(name='q[fuel_type][]',nr=1).get('{}'.format('')).selected=True
        # br.find_control(name='q[year_from][]').get('{}'.format('')).selected=True
        # br.find_control(name='q[year_to][]').get('{}'.format('')).selected=True
        br.submit()
        self.link = br.geturl()
