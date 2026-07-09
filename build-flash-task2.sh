python scripts/export_litert_baseline.py 
./firmware/build_firmware.sh
python host/run_submission.py   --task 2   --split validation   --source raw   --port /dev/ttyACM0   --uf2 firmware/build/vlp_pico.uf2