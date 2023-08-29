def get_year_choices():
    '''
    function that creates a tuple with choices
    for the year options
    '''
    current_year = 2023
    start_year = 1990
    return tuple((str(year), str(year)) for year in range(
        current_year, start_year - 1, -1))


BODY_TYPE = (
    ('convertable', 'Convertable'),
    ('coupe', 'Coupe'),
    ('saloon', 'Saloon'),
    ('hatchback', 'Hatchback'),
    ('estate', 'Estate'),
    ('mpv', 'MPV'),
    ('suv', 'SUV'),
    ('van', 'Van')
)

FUEL_TYPE = (
    ('petrol', 'Petrol'),
    ('diesel', 'Diesel'),
    ('hybrid', 'Hybrid'),
    ('electric', 'Electric'),
)

TRANSMISSION = (
    ('manual', 'Manual'),
    ('automatic', 'Automatic')
)

COUNTIES = (
    ('antrim', 'Antrim'),
    ('armagh', 'Armagh'),
    ('carlow', 'Carlow'),
    ('cavan', 'Cavan'),
    ('clare', 'Clare'),
    ('cork', 'Cork'),
    ('derry', 'Derry'),
    ('donegal', 'Donegal'),
    ('down', 'Down'),
    ('dublin', 'Dublin'),
    ('fermanagh', 'Fermanagh'),
    ('galway', 'Galway'),
    ('kerry', 'Kerry'),
    ('kildare', 'Kildare'),
    ('kilkenny', 'Kilkenny'),
    ('laois', 'Laois'),
    ('leitrim', 'Leitrim'),
    ('limerick', 'Limerick'),
    ('longford', 'Longford'),
    ('louth', 'Louth'),
    ('mayo', 'Mayo'),
    ('meath', 'Meath'),
    ('monaghan', 'Monaghan'),
    ('offaly', 'Offaly'),
    ('roscommon', 'Roscommon'),
    ('sligo', 'Sligo'),
    ('tipperary', 'Tipperary'),
    ('tyrone', 'Tyrone'),
    ('waterford', 'Waterford'),
    ('westmeath', 'Westmeath'),
    ('wexford', 'Wexford'),
    ('wicklow', 'Wicklow')
)

PRICE_OPTIONS = (
    ('1', '€1'),
    ('1000', '€1,000'),
    ('2000', '€2,000'),
    ('3000', '€3,000'),
    ('4000', '€4,000'),
    ('5000', '€5,000'),
    ('6000', '€6,000'),
    ('7000', '€7,000'),
    ('8000', '€8,000'),
    ('9000', '€9,000'),
    ('10000', '€10,000'),
    ('12500', '€12,500'),
    ('15000', '€15,000'),
    ('17500', '€17,500'),
    ('20000', '€20,000'),
    ('22500', '€22,500'),
    ('25000', '€25,000'),
    ('27500', '€27,500'),
    ('30000', '€30,000'),
    ('35000', '€35,000'),
    ('40000', '€40,000'),
    ('45000', '€45,000'),
    ('50000', '€50,000'),
    ('55000', '€55,000'),
    ('60000', '€60,000'),
    ('65000', '€65,000'),
    ('70000', '€70,000'),
    ('75000', '€75,000'),
    ('100000', '€100,000'),
    ('250000', '€250,000'),
    ('500000', '€500,000'),
)
