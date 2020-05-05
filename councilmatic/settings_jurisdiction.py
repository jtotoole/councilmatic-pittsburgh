import os

# These are all the settings that are specific to a jurisdiction

###############################
# These settings are required #
###############################

OCD_JURISDICTION_ID = 'ocd-jurisdiction/country:us/state:pa/place:pittsburgh'
OCD_CITY_COUNCIL_ID = 'ocd-jurisdiction/country:us/state:pa/place:pittsburgh/legislature'
OCD_CITY_COUNCIL_NAME = 'Pittsburgh City Council'
CITY_COUNCIL_NAME = 'Pittsburgh City Council'
LEGISLATIVE_SESSIONS = [str(year) for year in range(2001, 2021)]  # the second arg to range should be this year + 1
CITY_NAME = 'Pittsburgh'
CITY_NAME_SHORT = 'Pittsburgh'

# VOCAB SETTINGS FOR FRONT-END DISPLAY
CITY_VOCAB = {
    'MUNICIPAL_DISTRICT': 'District',  # e.g. 'District'
    'SOURCE': 'Pittsburgh City Clerk',
    'COUNCIL_MEMBER': 'Council Member',  # e.g. 'Council Member'
    'COUNCIL_MEMBERS': 'Council Members',  # e.g. 'Council Members'
    'EVENTS': 'Meetings',  # label for the events listing, e.g. 'Events'
}

APP_NAME = 'pittsburgh'

#########################
# The rest are optional #
#########################

# this is for populating meta tags
SITE_META = {
    'site_name': 'Pittsburgh Councilmatic',
    'site_desc': 'City Council, demystified. Keep tabs on Pittsburgh legislation, votes, & hearings.',
    'site_author': 'City of Pittsburgh',
    'site_url': '',  # TODO--e.g. 'https://chicago.councilmatic.org'
    'twitter_site': '@PghIP',  # e.g.
    'twitter_creator': '@PghIP',  # e.g.
}

LEGISTAR_URL = 'https://pittsburgh.legistar.com/Legislation.aspx'

# this is for the boundaries of municipal districts, to add
# shapes to posts & ultimately display a map with the council
# member listing. the boundary set should be the relevant
# slug from the ocd api's boundary service
# available boundary sets here: http://ocd.datamade.us/boundary-sets/
BOUNDARY_SET = ''  # e.g. 'chicago-wards-2015'

# this is for configuring a map of council districts using data from the posts
# set MAP_CONFIG = None to hide map
MAP_CONFIG = {
    'center': [40.4406, -79.9959],
    'zoom': 12,
    'color': "#54afe8",
    'highlight_color': "#C00000",
}

FOOTER_CREDITS = [
    {
        'name': 'City of Pittsburgh',  # e.g. 'DataMade'
        'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',  # e.g. 'http://datamade.us'
        # 'image':    '', # e.g. 'datamade-logo.png'
    },
]

# this is the default text in search bars
SEARCH_PLACEHOLDER_TEXT = 'Search council'  # e.g. 'police, zoning, O2015-7825, etc.'

# these should live in APP_NAME/static/
IMAGES = {
    'favicon': 'images/favicon.ico',
    'logo': 'images/website_logo.png',
}

# THE FOLLOWING ARE VOCAB SETTINGS RELEVANT TO DATA MODELS, LOGIC
# (this is diff from VOCAB above, which is all for the front end)

# this is the name of the meetings where the entire city council meets
# as stored in legistar
CITY_COUNCIL_MEETING_NAME = 'City Council'

# this is the name of the role of committee chairs, e.g. 'CHAIRPERSON' or 'Chair'
# as stored in legistar
# if this is set, committees will display chairs
COMMITTEE_CHAIR_TITLE = 'Chairperson'

# this is the anme of the role of committee members,
# as stored in legistar
COMMITTEE_MEMBER_TITLE = 'Member'

# this is for convenience, & used to populate a table
# describing legislation types on the default 'About' page template
LEGISLATION_TYPE_DESCRIPTIONS = [
    {
        'name': 'Appointment-Informing',
        'search_term': 'Appointment',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': '',
    },
    {
        'name': 'Appointment-Requiring Vote',
        'search_term': 'Appointment',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': '',
    },
    {
        'name': 'Certificate of Election',
        'search_term': 'Election',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': '',
    },
    {
        'name': 'Communication',
        'search_term': 'Communication',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': '',
    },
    {
        'name': 'Executive Order',
        'search_term': 'Executive Order',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': '',
    },
    {
        'name': 'Invoices',
        'search_term': 'Invoices',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': '',
    },
    {
        'name': 'Report',
        'search_term': 'Report',
        'fa_icon': 'dollar',
        'html_desc': True,
        'desc': 'Submissions of official reports by departments, boards and sister agencies.',
    },
    {
        'name': 'Petition',
        'search_term': 'Petition',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': '',
    },
    {
        'name': 'Post Agenda',
        'search_term': 'Post Agenda',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': '',
    },
    {
        'name': 'Proclamation',
        'search_term': 'Proclamation',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Public Hearing',
        'search_term': 'Public Hearing',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Remarks',
        'search_term': 'Remarks',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Report',
        'search_term': 'Report',
        'fa_icon': 'dollar',
        'html_desc': True,
        'desc': 'Submissions of official reports by departments, boards and sister agencies.',
    },
    {
        'name': 'Resolution',
        'search_term': 'Resolution',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Sister City Inventory',
        'search_term': 'Sister City',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Small Games of Chance',
        'search_term': 'Small Games of Chance',
        'fa_icon': 'dollar',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Transcripts - Public Hearing',
        'search_term': 'Transcripts - Public Hearing',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Transcripts - Regular Meeting',
        'search_term': 'Transcripts - Regular Meeting',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Transcripts - Special Council Meeting',
        'search_term': 'Transcripts - Special Council Meeting',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Veto Message',
        'search_term': 'Veto Message',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    },
    {
        'name': 'Will of Council',
        'search_term': 'Will of Council',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': ''
    }
]

# these keys should match committee slugs
COMMITTEE_DESCRIPTIONS = {
    # e.g. "committee-on-aviation" : "The Committee on Aviation has jurisdiction over matters relating to aviation and airports.",
    "committee-on-finance-and-law-55316b639785": "The Committee on Finance and Law has charge of and jurisdiction "
                                                 "over all ordinances, resolutions, bills, papers and other matters "
                                                 "relating to: Bonds and Debt Issuance; City Banking/Investment; "
                                                 "Creation of Offices or Positions of any kind; Department of "
                                                 "Finance; Enterprise Resource System; Equal Opportunity "
                                                 "Review Commission (EORC); Ethics; Law Department; Multi-year Capital "
                                                 "Improvement Program; Office of Management and Budget (OMB) "
                                                 "Operating & Capital Budgets; Pension Fiscal; Real Estate; Taxation; "
                                                 "Treasurer and such other business as may be referred to it by the "
                                                 "Council, provided, however, that where money has been specifically "
                                                 "appropriated by the Council for any of the purposes of the "
                                                 "departments of the City government, that said committee "
                                                 "shall then have complete charge and jurisdiction.",
    "committee-on-public-safety-services-95b1a09a5422": "The Committee on Public Safety Services has charge of and "
                                                        "jurisdiction over all ordinances, resolutions, bills, "
                                                        "papers, and other matters of every kind pertaining to: "
                                                        "Bureau of Animal Control; Permits; Licenses & Inspections; "
                                                        "Bureau of Fire; Bureau of Police; Citizens Police Review "
                                                        "Board (CPRB); Department of Public Safety; Emergency "
                                                        "Management Agency (EMA); Emergency Medical Services (EMS); "
                                                        "Emergency Operations and Communications; Homeland Security; "
                                                        "Weed and Seed.",
    "committee-on-public-works-13c20b3f6ec8": "The Committee on Public Works has charge of and jurisdiction over all "
                                              "ordinances, resolutions, bills, or papers affecting or pertaining to: "
                                              "Bureau of Administration; Bureau of Engineering, Bureau of "
                                              "Environmental Services, Bureau of Operations, Construction, Department "
                                              "of Public Works, Environmental Services and Control, Facilities "
                                              "Operation and Maintenance (Not Parks or Recreation related), Forestry, "
                                              "Franchises and Rights of Way to Corporations, Public Right-of-Way "
                                              "Maintenance, Shade Tree, Streets Lighting.",
    "committee-on-human-resources-2faa03a67605": "The Committee on Human Resources has charge of and jurisdiction "
                                                 "over all ordinances, resolutions, bills, or papers affecting or "
                                                 "pertaining to: Benefits; Department of Personnel and Civil Service; "
                                                 "Equal Employment Opportunity Commission (EEOC); Human Relations "
                                                 "Commission (HRC); Job Training Partnership Act (JTPA); Office of "
                                                 "Municipal Investigation (OMI); Payroll Administration/System; "
                                                 "Pension Benefits Administration; Personnel (inclusive of "
                                                 "Salaries and Employment Numbers).",
    "committee-on-urban-recreation-eb94f0bcae13": "The Committee on Urban Recreation has charge of and jurisdiction "
                                                  "over all ordinances, resolutions, bills, or papers pertaining to: "
                                                  "Department of Parks and Recreation (CitiParks); Greenways; Libraries;"
                                                  " Park Programming; Recreation Facilities Maintenance; Senior "
                                                  "Centers; Programming and Advisory Council; Special Events; Trails; "
                                                  "Youth Policy.",
    "committee-on-innovation-performance-and-asset-management-a9c848628cb5": "The Committee on Innovation, "
                                                                             "Performance and Asset Management has "
                                                                             "charge of and jurisdiction over all "
                                                                             "ordinances, resolutions, bills, papers, "
                                                                             "and other matters relating to: 311 "
                                                                             "Mayor's Response Center; City Cable "
                                                                             "Channel; Department of Innovation & "
                                                                             "Performance; Facilities Inventory and "
                                                                             "Management; Fleet Maintenance, "
                                                                             "Repair, and Alteration; Purchasing and B "
                                                                             "Contracts; Information Technology; Data "
                                                                             "Collection and Analysis; Operational "
                                                                             "Performance Targets; Sustainabillity "
                                                                             "Initiatives; Professional Management Systems",
    "committee-on-intergovernmental-affairs-ea2536579769": "The Committee on Intergovernmental Affairs has charge of "
                                                           "and jurisdiction over all ordinances, resolutions, bills, "
                                                           "or papers affecting or pertaining to: Allegheny Regional Assets "
                                                           "District (ARAD); Authorities - Agreements; County; Federal; Local "
                                                           "governmental cooperation agreements; Liquor Licenses; Pennsylvania "
                                                           "League of Cities and Municipalities; Port of Pittsburgh; School "
                                                           "Boards; State; Tourism - Visit Pittsburgh.",
    "committee-on-hearings-129c372efefc": "The Committee on Hearings has charge of the jurisdiction and scheduling of: "
                                          "Appointments and Reappointments; Executive Sessions; Public Hearings; "
                                          "Public Meetings.",
}

# these blurbs populate the wells on the committees, events, & council members pages
ABOUT_BLURBS = {
    "COMMITTEES": "",
    "EVENTS": "",
    "COUNCIL_MEMBERS": "",
}

# these override the headshots that are automatically populated
# the keys should match a person's slug

MANUAL_HEADSHOTS = {
    'william-peduto-03a1cbeed289': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/peduto.png'},
    'reverend-ricky-v-burgess-e6be10da476b': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/burgess.jpg'},
    'anthony-coghill-c227693ce28c': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/coghill.jpg'},
    'deborah-l-gross-36696a2838ea': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/gross.jpg'},
    'bobby-wilson-8d4fc4fb499e': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/wilson.jpg'},
    'theresa-kail-smith-d8e06c1f56c0': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/smith.jpg'},
    'bruce-a-kraus-98881f116f97': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/kraus.jpg'},
    'r-daniel-lavelle-18f0114e8773': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/lavelle.jpg'},
    'corey-oconnor-8993bcfc8d11': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/oconnor.jpg'},
    'erika-strassburger-fc76f94ccd73': {'source': 'pittsburghpa.gov', 'image': 'manual-headshots/strassburger.jpg'},
}

CONTACT_INFO = {
    'william-peduto-03a1cbeed289': {'twitter': {'handle': '@billpeduto', 'url': 'https://twitter.com/billpeduto'},
                                    'phone': '', 'website': 'https://pittsburghpa.gov/mayor/mayor-profile',
                                    'email': ''},
    'reverend-ricky-v-burgess-e6be10da476b': {
        'twitter': {'handle': '@RevBurgessPgh', 'url': 'https://twitter.com/RevBurgessPgh'},
        'phone': '412-255-2137/412-255-8658', 'email': 'reverend.burgess@pittsburghpa.gov',
        'website': 'https://pittsburghpa.gov/council/burgess'},
    'anthony-coghill-c227693ce28c': {
        'twitter': {'handle': '@CoghillAnthony', 'url': 'https://twitter.com/CoghillAnthony'},
        'phone': '412-255-2131', 'email': 'kaitlyn.fisher@pittsburghpa.gov',
        'website': 'https://pittsburghpa.gov/council/coghill'},
    'deborah-l-gross-36696a2838ea': {'twitter': {'handle': '@DebGrosspgh', 'url': 'https://twitter.com/DebGrosspgh'},
                                     'phone': '412-255-2140', 'email': 'district7@pittsburghpa.gov',
                                     'website': 'https://pittsburghpa.gov/council/gross'},
    'bobby-wilson-8d4fc4fb499e': {'twitter': {'handle': '@bobbywilson412', 'url': 'https://twitter.com/bobbywilson412'},
                                  'phone': '412-255-2135', 'email': '',
                                  'website': 'https://pittsburghpa.gov/council/d1'},
    'theresa-kail-smith-d8e06c1f56c0': {'twitter': {'handle': '@tkailsmith', 'url': 'https://twitter.com/tkailsmith'},
                                        'phone': '412-255-8963', 'email': 'jill.harris@pittsburghpa.gov',
                                        'website': 'https://pittsburghpa.gov/council/kail-smith'},
    'bruce-a-kraus-98881f116f97': {'twitter': {'handle': '@BruceKraus', 'url': 'https://twitter.com/BruceKraus'},
                                   'phone': '412-255-2130', 'email': 'robert.charland@pittsburghpa.gov',
                                   'website': 'https://pittsburghpa.gov/council/kraus'},
    'r-daniel-lavelle-18f0114e8773': {'twitter': {'handle': '@RDLavelle', 'url': 'https://twitter.com/RDLavelle'},
                                      'phone': '412-255-2134', 'email': 'cassandra.williams@pittsburghpa.gov',
                                      'website': 'https://pittsburghpa.gov/council/lavelle'},
    'corey-oconnor-8993bcfc8d11': {
        'twitter': {'handle': '@CoreyOConnorPGH', 'url': 'https://twitter.com/CoreyOConnorPGH'},
        'phone': '412-255-8965', 'email': 'connie.sukernek@pittsburghpa.gov',
        'website': 'https://pittsburghpa.gov/council/oconnor'},
    'erika-strassburger-fc76f94ccd73': {
        'twitter': {'handle': '@erikastrassbrgr', 'url': 'https://twitter.com/erikastrassbrgr'},
        'phone': '412-255-2133', 'email': 'erika.strassburger@pittsburghpa.gov',
        'website': 'https://pittsburghpa.gov/council/strassburger'},
}
# notable positions that aren't district representatives, e.g. mayor & city clerk
# keys should match person slugs
EXTRA_TITLES = {
    'william-peduto-03a1cbeed289': 'Mayor',
}

USING_NOTIFICATIONS = True
