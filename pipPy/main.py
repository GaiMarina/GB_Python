
import StringIO
import Csv2Xml

buff = StringIO(csv_str)
print buff # doctest:+ELLIPSIS
StringIO.StringIO ...>

csv_convertor = Csv2Xml(buff, delimiter = ";") # doctest:+ELLIPSIS
print csv_convertor.as_string()