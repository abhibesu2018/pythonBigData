import argparse
from pyspark import SparkConf,SparkContext
from pyspark.sql.session import SparkSession

parser = argparse.ArgumentParser()
parser.add_argument("--accessKeyId", help="Input accesskey id.")
parser.add_argument("--secretAccessKey", help="Input secret accesskey")
args = parser.parse_args()
if args.accessKeyId:
	accessKeyId=args.accessKeyId
if args.secretAccessKey:
	secretAccessKey=args.secretAccessKey


sc_conf = SparkConf()
sc_conf.setAppName("Abhi App")
sc_conf.set("spark.shuffle.service.enabled", "false")
sc_conf.set("spark.dynamicAllocation.enabled", "false")
sc = SparkContext(conf=sc_conf)
sc.setLogLevel("INFO")
spark = SparkSession(sc)
#a = spark.read.csv("hdfs://localhost:9000/input/transportation-department-permits.csv")
sc._jsc.hadoopConfiguration().set("fs.s3n.awsAccessKeyId", accessKeyId)
sc._jsc.hadoopConfiguration().set("fs.s3n.awsSecretAccessKey", secretAccessKey)

a = spark.read.csv("s3n://abhibesu-poc/resources/transportation-department-permits.csv")
print("**************************************************************************")
print("Count of records: ", a.count())


sc.stop()
