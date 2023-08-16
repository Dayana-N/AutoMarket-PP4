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
