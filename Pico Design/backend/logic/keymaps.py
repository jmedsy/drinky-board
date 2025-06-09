from collections import namedtuple

Pin = namedtuple('Pin', ['addr', 'logipin'])
Mapping = namedtuple('Mapping', ['row', 'col'])

escape = Mapping(
    row=Pin(addr=0x70, logipin=5),
    col=Pin(addr=0x71, logipin=12),
)
