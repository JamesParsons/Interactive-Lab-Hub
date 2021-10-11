from subprocess import Popen, PIPE, STDOUT

text = u"René Descartes"
p = Popen(['espeak', '-b', '1'], stdin=PIPE, stdout=DEVNULL, stderr=STDOUT)