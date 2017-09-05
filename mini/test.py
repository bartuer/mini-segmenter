# -*- coding: utf8 -*-
import minisegmenter as mini
import sys;
reload(sys);
sys.setdefaultencoding('utf8')
for line in sys.stdin:
    print mini.segmenter(line.decode('utf8'))
