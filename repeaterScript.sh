# COMMANF TO CONVERT TO UNIX FORMAT
# sed -i 's/\r$//' ./repeaterScript.sh
# nohup ./repeaterScript.sh < input.txt > output.txt &

# ps xw

echo "Enter the number of the script you want to run: "
echo "1. KMeans Training"
echo "2. Random Forest Training"
echo "3. W2V Training"
echo "Enter your option: "
read option

echo "Enter the number of times you want to run the script: "
read n

for i in $(seq 1 $n)
do
echo "Starting iteration $i:"
if [ $option -eq 1 ]; then
echo "Running KMeans Training..."
python3.8 kmeans_training.py
elif [ $option -eq 2 ]; then
echo "Running Random Forest Training..."
python3.8 random_forest_training.py
elif [ $option -eq 3 ]; then
echo "Running W2V Training..."
python3.8 w2v_training.py
else
echo "Invalid option selected. Please try again."
exit 1
fi
echo "Finished iteration $i."
echo " "
done

echo "All iterations complete."