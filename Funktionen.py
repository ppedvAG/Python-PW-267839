import pandas as pd

# Funktionen
# Code wiederverwenden
# -> Code in Funktionen speicher, und diese später verwenden

# def
# Legt eine neue Funktion an
# Syntax: def <Name>(<Parameterliste>)
def hallo():
    print("Hallo Welt")

hallo() # der Code innerhalb von hallo() wird hier ausgeführt
hallo()
hallo()

# die 2. Funktion hallo(name="Welt") überschreibt die erste Funktion hallo() komplett
# unten existiert die 1. Funktion nicht mehr

# Parameter
# an Funktionen Daten mitgeben können
# Beliebig viele Variablennamen in der Klammer definieren
def hallo(name = "Welt"): # default Value für name ist Welt, also ist name optional
    print(f"Hallo {name}")
    # Je nach Parameter hat der Aufruf dieser Funktion verschiedene Auswirkungen

hallo("Lukas")
hallo("Sarah")
hallo()

# return
# gibt einen Wert an die aufrufende Instanz zurück
# also dort hin wo die Funktion aufgerufen wird.
# return beendet außerdem die Funktion
def addieren(x, y):
    return x + y
    print(x+y) # code hier ist unreachable, weil return die Funktion beendet

print("Zahl eingeben:")
x = float(input())

print("Zahl eingeben:")
y = float(input())

print(addieren(x,y))

print(addieren(10,20))
print(addieren(5,7))

# Nachteil: Parameter in Python können beliebige Daten empfangen
# Wir können den User der Funktion nicht abhalten, beliebige, fehlerhafte Daten einzugeben
print(addieren(3,4))
print(addieren(3.5,20.4))
print(addieren("Hallo","Welt"))
print(addieren([10,54],[4,5,20]))
print(addieren(True, True))

# Typempfehlung
# Bei Parametern den gewünschten Typen angeben
# WICHTIG: User kann weiterhin beliebige Daten eingeben
def subtrahieren(x:int|float, y:int|float):
    return x-y

print(subtrahieren(121,1)) # Empfehlung wird beim eingeben angezeigt.
print(subtrahieren(3.4,4.5))
#print(subtrahieren(3,"hallo")) # ich kann Falscheingaben nicht verhindern

# Typvergleich
# Prüft per if, ob die Variable tatsächlich den korrekten Typen hat
# "streng"
def multipliziere(x:int|float, y:int|float):
    # Überprüfung von x und y sind logisch identisch, type(x) in [int, float] ist kürzer
    if(type(x) in [int, float] and (type(y) == int or type(y) == float)):
        print(f"{x} * {y} = {x*y}")
    else:
        raise TypeError("X und Y müssen Zahlen sein!") # raise lässt das Programm abstürzen

multipliziere(3.4,4)
# multipliziere("3.4",4.5) # wirft Error mit unserer Fehlermeldung


# Rückgabewerte
# Ergebnis einer Funktion zurückgeben
# Dieses Ergebnis kann in eine Variable geschrieben und weiterverarbeitet werden
text = "Ich bin ein Text"
s = text.split(" ")
print(s)
u = text.upper()
print(u)

# Default Parameter
# Standardwerte für Parameter
# Können überschieben werden oder auch nicht
def dividiere(x:int|float, y:int|float = 2):
    if y == 0:
        raise ZeroDivisionError("Division durch 0") # wird eigentlich sowieso geworfen, hier mit extra deutscher Fehlermeldung
    return x/y


print(dividiere(3.4,4.5))
print(dividiere(3.4))
print(dividiere(3.4, 0))


# Funktionen konfigurieren
# In Python gibt es sehr viele Funktionen, die 10, 20, 30,... Parameter haben
# Fast alle (oder alle) dieser Parameter sind optional
# Über den Namen des Parameters kann dann genau dieser verändert werden
# Es müssen nicht alle Parameter angegeben werden, sonder nur die benötigten

# Beispiel: pandas.read_csv
# pandas.read_csv(filepath_or_buffer: str | PathLike[str] | ReadCsvBuffer[bytes] | ReadCsvBuffer[str], *,
#              sep: Any = lib.no_default,
#              delimiter: Any | None = None,
#              header: int | Sequence[int] | None | Literal["infer"] = "infer",
#              names: Any = lib.no_default,
#              index_col: Hashable | Sequence[Hashable] | Literal[False] | None = None,
#              usecols: SequenceNotStr[Hashable] | range | ExtensionArray | ndarray[tuple[Any, ...], dtype[Any]] | Index | Series | (HashableT) -> bool | None = None,
#              dtype: ExtensionDtype | str | dtype[Any] | type[str] | type[complex] | type[bool] | type[object] | Mapping[Hashable, ExtensionDtype | str | dtype[Any] | type[str] | type[complex] | type[bool] | type[object]] | None = None,
#              engine: Literal["c", "python", "pyarrow", "python-fwf"] | None = None,
#              converters: Mapping[HashableT, (...) -> Any] | None = None,
#              true_values: list | None = None,
#              false_values: list | None = None,
#              skipinitialspace: bool = False,
#              skiprows: list[int] | int | (Hashable) -> bool | None = None,
#              skipfooter: int = 0,
#              nrows: int | None = None,
#              na_values: Hashable | Iterable[Hashable] | Mapping[Hashable, Iterable[Hashable]] | None = None,
#              keep_default_na: bool = True,
#              na_filter: bool = True,
#              skip_blank_lines: bool = True,
#              parse_dates: bool | Sequence[Hashable] | None = None,
#              date_format: str | dict[Hashable, str] | None = None,
#              dayfirst: bool = False,
#              cache_dates: bool = True,
#              iterator: bool = False,
#              chunksize: int | None = None,
#              compression: Literal["infer", "gzip", "bz2", "zip", "xz", "zstd", "tar"] | dict[str, Any] | None = "infer",
#              thousands: str | None = None,
#              decimal: str = ".",
#              lineterminator: str | None = None,
#              quotechar: str = '\"',
#              quoting: int = csv.QUOTE_MINIMAL,
#              doublequote: bool = True,
#              escapechar: str | None = None,
#              comment: str | None = None,
#              encoding: str | None = None,
#              encoding_errors: str | None = "strict",
#              dialect: str | Dialect | None = None,
#              on_bad_lines: str = "error",
#              low_memory: bool = _c_parser_defaults["low_memory"],
#              memory_map: bool = False,
#              float_precision: Literal["high", "legacy", "round_trip"] | None = None,
#              storage_options: dict[str, Any] | None = None,
#              dtype_backend: Any = lib.no_default)

#
def read_csv(
    filepath_or_buffer,
    sep = ";",
    delimiter = ";",
    header = True):
    print()

# Hier werden jetzt nur die benötigten Parameter angegeben
read_csv("Beispeilpfad", ",")
read_csv("Beispeilpfad", header=False)
read_csv("Beispeilpfad", sep=";", header=False)



