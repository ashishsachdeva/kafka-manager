import sys

def override_configs(confs):
  config_file = "/usr/local/kafka-manager/kafka-manager-1.3.3.8/conf/application.conf"
  kafka_manager_zookeeper = confs["KAFKA_BOOTSTRAP_SERVERS"].split(':')[0]
  import subprocess
  cmd='sed -i "s:kafka-manager-zookeeper:' + kafka_manager_zookeeper + ':g" /usr/local/kafka-manager/kafka-manager-1.3.3.8/conf/application.conf'
  subprocess.Popen(cmd, shell=True).wait()
   
def main():
  confs = {}
  for x in range(1,len(sys.argv)):
    if sys.argv[x].startswith("KAFKA"):
      (k, v) = sys.argv[x].split("=", 1)
      confs[k] = v
    else:
      print "Ignoring " + sys.argv[x] + " as it does not start with KAFKA_"

  override_configs(confs)

if __name__ == "__main__":
  main()

