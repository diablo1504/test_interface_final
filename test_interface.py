# coding=utf-8
import random
import unittest
import time
import HTMLTestRunner
import md5
import hashlib
import hmac
import urllib,urllib2
import json
import xlrd
import os

KEY_TIME = "_time"
KEY_AK = "_ak"
PARAMS_SEP = "&"
ACCESS_KEY = "superlvr"
SECRET_KEY = "fa034ce350e72d8a3960ba560150cd62"
timestamp = time.time()

def getSignature(accessKey, secretKey, params, time):
    sin = []
    sin.append(KEY_TIME + "=" + str(timestamp)) # May...
    sin.append(KEY_AK + "=" + accessKey)
    if params != None:
        for kk in params:
            params_fm = kk + "=" + urllib.quote(str(params[kk]))
            sin.append(params_fm)
    sin.sort()
    paramstring = joinSep(sin, PARAMS_SEP)
    print "paramstring as: " + paramstring
    strSign = paramstring + secretKey
    print "strSign as: " + strSign
    md = md5.new()
    md.update(strSign)
    strSignature = md.hexdigest()
    #print "strSignature as: " + strSignature
    return strSignature, paramstring

def joinSep(arr_str, sep):
    new_str = ""
    first = True
    for s in arr_str:
        if first:
            first = False
        else:
            new_str = new_str + sep
        new_str = new_str + s
    return new_str

def testsMain():
    header = eval(cell_value5)
    data = None
    values = cell_value6
    url = cell_value3
    par = eval(cell_value4)
    my_string = par
    method = cell_value7
    method = method.lower()
    if method == "get":
        if "<" and ">" in url:
            for i in par.keys():
                n_p_k = "<" + str(i) + ">"
                if n_p_k in url:
                    url = url.replace(n_p_k, str(par[i]))
                    par.pop(i)
        elif "{" and "}" in url:
            for i in par.keys():
                n_p_k = "{" + str(i) + "}"
                if n_p_k in url:
                    url = url.replace(n_p_k, str(par[i]))
                    par.pop(i)
        return_items = getSignature(ACCESS_KEY, SECRET_KEY, par, time)
        _sign = return_items[0]
        strpar = return_items[1]
        my_string = strpar + "&_sign=" + _sign
        url2 = url + '?' + my_string
        print "url2 as: " + url2
        req = urllib2.Request(url2, data, header)
        res_data = urllib2.urlopen(req)
        apicontent = res_data.read()
        j_a_c = json.loads(apicontent)
        result = json.dumps(j_a_c, indent=4)
        file_object = open('E:\\test_result\\pro.txt', 'w')
        file_object.write(result)
        file_object.close()
        try:
            print "actual result:\n" + result.decode("unicode_escape")
        except:
            pass
    elif method == "post":
        if "<" and ">" in url:
            for i in par.keys():
                n_p_k = "<" + str(i) + ">"
                if n_p_k in url:
                    url = url.replace(n_p_k, str(par[i]))
                    par.pop(i)
        return_items = getSignature(ACCESS_KEY, SECRET_KEY, par, time)
        _sign = return_items[0]
        strpar = return_items[1]
        my_string = strpar + "&_sign=" + _sign
        # #my_string = strpar
        # url2 = url + '?' + my_string
        # print "url2 as: " + url2
        # data = urllib.urlencode(values)
        # req = urllib2.Request(url2,data,header)
        req = urllib2.Request(url, my_string,header)
        res_data = urllib2.urlopen(req)
        apicontent = res_data.read()
        j_a_c = json.loads(apicontent)
        result = json.dumps(j_a_c, indent=4)
        file_object = open('E:\\test_result\\pro.txt', 'w')
        file_object.write(result)
        file_object.close()
        try:
            print "actual result:\n" + result.decode("unicode_escape")
        except:
            pass
    elif method == "put":
        if "<" and ">" in url:
            for i in par.keys():
                n_p_k = "<" + str(i) + ">"
                if n_p_k in url:
                    url = url.replace(n_p_k, str(par[i]))
                    par.pop(i)
        return_items = getSignature(ACCESS_KEY, SECRET_KEY, par, time)
        _sign = return_items[0]
        strpar = return_items[1]
        my_string = strpar + "&_sign=" + _sign
        url2 = url + '?' + my_string
        print "url2 as: " + url2
        req = urllib2.Request(url2, data, header)
        req.get_method = lambda: 'PUT'
        res_data = urllib2.urlopen(req)
        apicontent = res_data.read()
        j_a_c = json.loads(apicontent)
        result = json.dumps(j_a_c, indent=4)
        file_object = open('E:\\test_result\\pro.txt', 'w')
        file_object.write(result)
        file_object.close()
        try:
            print "actual result:\n" + result.decode("unicode_escape")
        except:
            pass
    elif method == "delete":
        if "<" and ">" in url:
            for i in par.keys():
                n_p_k = "<" + str(i) + ">"
                if n_p_k in url:
                    url = url.replace(n_p_k, str(par[i]))
                    par.pop(i)
        return_items = getSignature(ACCESS_KEY, SECRET_KEY, par, time)
        _sign = return_items[0]
        strpar = return_items[1]
        my_string = strpar + "&_sign=" + _sign
        url2 = url + '?' + my_string
        print "url2 as: " + url2
        req = urllib2.Request(url2, data, header)
        req.get_method = lambda: 'DELETE'
        res_data = urllib2.urlopen(req)
        apicontent = res_data.read()
        j_a_c = json.loads(apicontent)
        result = json.dumps(j_a_c, indent=4)
        file_object = open('E:\\test_result\\pro.txt', 'w')
        file_object.write(result)
        file_object.close()
        try:
            print "actual result:\n" + result.decode("unicode_escape")
        except:
            pass
    else:
        print "\t... hehe ..."
    return result

class TestDictValueFormatFunctions(unittest.TestCase):
    def setUp(self):
        testsMain()
        file_object = open('E:\\test_result\\pro.txt', 'rb')
        list_of_all_the_lines = file_object.read()
        ccc = json.loads(list_of_all_the_lines)
        ddd = json.dumps(ccc, indent=4)
        eee = eval(ddd)
        fff = []
        fff.append(eee["data"])
        self.results = fff
    def test_format(self):
        self.assertTrue(isinstance(self.results, list),
                        "self.results's type must be dict but got {0}".format(type(self.results)))
        for r in self.results:
            for f in results_fields_map:
                value = r.get(f, None)
                self.assertTrue(isinstance(value, results_fields_map[f]),
                                u"{0}'s type must be {1} but got {2}".format(value, results_fields_map[f], type(value)))
                # self.assertTrue(isinstance(value, results_fields_map[f]))

    def test_value(self):
        for r in self.results:
            self.assertEqual(r["versionCode"], "16113002")
            self.assertEqual(r["sysVersionCode"], "16061320")
class TestDictValueFormatFunctions(unittest.TestCase):
    def setUp(self):
        testsMain()
        file_object = open('E:\\test_result\\pro.txt', 'rb')
        list_of_all_the_lines = file_object.read()
        ccc = json.loads(list_of_all_the_lines)
        ddd = json.dumps(ccc, indent=4)
        eee = eval(ddd)
        fff = []
        fff.append(eee["data"])
        self.results = fff
    def test_format(self):
        self.assertTrue(isinstance(self.results, list),
                        "self.results's type must be dict but got {0}".format(type(self.results)))
        for r in self.results:
            for f in results_fields_map:
                value = r.get(f, None)
                self.assertTrue(isinstance(value, results_fields_map[f]),
                                u"{0}'s type must be {1} but got {2}".format(value, results_fields_map[f], type(value)))
                # self.assertTrue(isinstance(value, results_fields_map[f]))

    def test_value(self):
        for r in self.results:
            self.assertEqual(r["versionCode"], "16113002")
            self.assertEqual(r["sysVersionCode"], "16061320")

if __name__ == '__main__':
    fname = "APIcase222.xlsx"
    bk = xlrd.open_workbook(fname)
    sheet_list = bk.sheets()
    shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name("real")
    except:
        print "no sheet in %s named Sheet1" % fname
    # 获取行数
    nrows = sh.nrows
    # 获取列数
    ncols = sh.ncols
    print "nrows %d, ncols %d" % (nrows, ncols)
    # 获取数据
    # for i in range(102,113):
    t_now = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    for i in range(1, 3):  # 目标起始行所在的前一行到目标结尾行
        print '------------------------------------------------------------------------------------------------------------------'
        try:
            cell_value1 = sh.cell_value(i, 1)
            cell_value2 = sh.cell_value(i, 6)
            cell_value3 = sh.cell_value(i, 2)
            cell_value4 = sh.cell_value(i, 3)
            cell_value5 = sh.cell_value(i, 4)
            cell_value6 = sh.cell_value(i, 5)
            cell_value7 = sh.cell_value(i, 7)
            # filename = cell_value1+cell_value2
            # print filename
            result_dir = 'C:\\Users\\wujingjian\\Desktop\\result\\%s\\%s' % (t_now, cell_value1)
            os.makedirs(result_dir)
        except:
            pass
        try:
            output = open(result_dir + '\\%s.txt' % cell_value2, 'w')
            output.write(testsMain())
        except Exception, e:
            output = open(result_dir + '\\%s.txt' % cell_value2, 'w')
            output.write(str(e))
        output.close()
        utf8string = cell_value6.encode("utf-8")
        utf8string_change = eval(utf8string)
        results_fields = utf8string_change
        results_fields_map = dict(results_fields)

        suite2 = unittest.TestLoader().loadTestsFromTestCase(TestDictValueFormatFunctions)
        suite = unittest.TestSuite(suite2)
        # 获取当前时间，这样便于下面的使用。
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        # 打开一个文件，将result写入此file中
        fp = open("E:\\test_result\\result" + now + ".html", 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:')
        runner.run(suite)
        fp.close()



