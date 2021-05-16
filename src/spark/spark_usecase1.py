from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, NumericType
from pyspark.sql.functions import sum
from pyspark.sql.functions import col

spark = SparkSession \
        .builder \
        .appName("Use case 1 - Number of movies that each platform have") \
        .getOrCreate()
dataset_dir = "gs://movies_bucket_spark/csv/"

# Reduce logging levels 
logger = spark._jvm.org.apache.log4j
logger.LogManager.getLogger("org"). setLevel(logger.Level.ERROR)
logger.LogManager.getLogger("akka").setLevel(logger.Level.ERROR)

df = spark \
    .read \
    .option("header", "true") \
    .option("inferSchema", "false") \
    .csv(dataset_dir + "MoviesOnStreamingPlatforms_clean.csv")

dftypes = df \
        .withColumn("Netflix", df["Netflix"].cast(IntegerType())) \
        .withColumn("Hulu", df["Hulu"].cast(IntegerType())) \
        .withColumn("Prime_Video", df["Prime_Video"].cast(IntegerType())) \
        .withColumn("Disney_plus", df["Disney_plus"].cast(IntegerType())) 

# dftypes.show()

netflixFilter = dftypes.filter(dftypes.Netflix == 1) 
huluFilter = dftypes.filter(dftypes.Hulu == 1) 
PrimeFilter = dftypes.filter(dftypes.Prime_Video == 1)
DisneyFilter = dftypes.filter(dftypes.Disney_plus == 1)       

netflixFilter.select(sum("Netflix")).show()
huluFilter.select(sum("Hulu")).show()
PrimeFilter.select(sum("Prime_Video")).show()
DisneyFilter.select(sum("Disney_plus")).show()

spark.stop()