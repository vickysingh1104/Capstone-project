{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f46f3f2d-ff83-47df-a778-bda9d1bfc99f",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'Capstone.pkl'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 5\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mnumpy\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mnp\u001b[39;00m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;66;03m# Load the pre-trained model from a file\u001b[39;00m\n\u001b[1;32m----> 5\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mopen\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mCapstone.pkl\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mrb\u001b[39m\u001b[38;5;124m'\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m file:\n\u001b[0;32m      6\u001b[0m     model \u001b[38;5;241m=\u001b[39m pickle\u001b[38;5;241m.\u001b[39mload(file)\n\u001b[0;32m      8\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mget_user_input\u001b[39m():\n\u001b[0;32m      9\u001b[0m     \u001b[38;5;66;03m# Define the features expected by the model\u001b[39;00m\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:310\u001b[0m, in \u001b[0;36m_modified_open\u001b[1;34m(file, *args, **kwargs)\u001b[0m\n\u001b[0;32m    303\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m2\u001b[39m}:\n\u001b[0;32m    304\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[0;32m    305\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mIPython won\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m by default \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    306\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    307\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124myou can use builtins\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m open.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    308\u001b[0m     )\n\u001b[1;32m--> 310\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m io_open(file, \u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'Capstone.pkl'"
     ]
    }
   ],
   "source": [
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "# Load the pre-trained model from a file\n",
    "with open('Capstone.pkl', 'rb') as file:\n",
    "    model = pickle.load(file)\n",
    "\n",
    "def get_user_input():\n",
    "    # Define the features expected by the model\n",
    "    feature_names = ['Age', 'Cholesterol', 'Heart Rate', 'Diabetes', 'Family History',\n",
    "       'Smoking', 'Obesity', 'Alcohol Consumption', 'Exercise Hours Per Week',\n",
    "       'Previous Heart Problems', 'Medication Use', 'Stress Level',\n",
    "       'Sedentary Hours Per Day', 'Income', 'BMI', 'Triglycerides',\n",
    "       'Physical Activity Days Per Week', 'Sleep Hours Per Day', 'High_BP ',\n",
    "       'Low_BP', 'Sex_Male', 'Diet_Healthy', 'Diet_Unhealthy',\n",
    "       'Hemisphere_Southern Hemisphere']  # Update with your feature names\n",
    "    \n",
    "    # Initialize an empty list to store the feature values\n",
    "    features = []\n",
    "    \n",
    "    # Prompt the user to enter values for each feature\n",
    "    for feature in feature_names:\n",
    "        while True:\n",
    "            try:\n",
    "                value = float(input(f\"Enter value for {feature}: \"))\n",
    "                features.append(value)\n",
    "                break\n",
    "            except ValueError:\n",
    "                print(\"Invalid input. Please enter a numeric value.\")\n",
    "    \n",
    "    return np.array([features])\n",
    "\n",
    "def main():\n",
    "    # Get user input for the features\n",
    "    user_features = get_user_input()\n",
    "    \n",
    "    # Predict the target using the pre-trained model\n",
    "    prediction = model.predict(user_features)\n",
    "    \n",
    "    # Output the predicted target\n",
    "    print(f\"The predicted target is: {prediction[0]}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "062eb041-57c7-417c-824c-af31fc4f8840",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
