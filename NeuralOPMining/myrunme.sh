nohup python -u driver/Train.py --config_file expdata/opinion.cfg --thread 4 > test_opinion.log 2>&1 &

tail -f test_opinion.log
