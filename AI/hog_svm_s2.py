###############################################
import cv2
import numpy as np

# Function to compute HOG features
def compute_hog_features(img, hog_descriptor):
    h = hog_descriptor.compute(img)
    return h

# Initialize the HOG descriptor
hog = cv2.HOGDescriptor()

# Prepare feature vectors and labels
features = []
labels = []

# Prepare training data
# Assuming you have lists of file paths for positive and negative samples
p_images = ['p1_1.png', 'p1_2.png', 'p1_3.png']
c_images = ['car1_1.png', 'car1_2.png', 'car1_3.png']
d_images = ['d1_1.png', 'd1_2.png', 'd1_3.png']

for img_path in d_images:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (64, 128))  # Resize image to the size used by HOG
    h = compute_hog_features(img, hog)
    features.append(h)
    labels.append(2)  # Label for positive samples

for img_path in p_images:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (64, 128))  # Resize image to the size used by HOG
    h = compute_hog_features(img, hog)
    features.append(h)
    labels.append(1)  # Label for positive samples

for img_path in c_images:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (64, 128))
    h = compute_hog_features(img, hog)
    features.append(h)
    labels.append(0)  # Label for negative samples

# Convert to numpy arrays
features = np.array(features, dtype=np.float32)
features = features.reshape(len(features), -1)  # Reshape for SVM input
labels = np.array(labels)

# Create and train the SVM
svm = cv2.ml.SVM_create()
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setType(cv2.ml.SVM_C_SVC)
svm.setC(0.01)
svm.setTermCriteria((cv2.TERM_CRITERIA_MAX_ITER, 100, 1e-6))

# Train the SVM
svm.train(features, cv2.ml.ROW_SAMPLE, labels)

# Save the trained SVM
svm.save('hog_svm_model.yml')

# To use the trained SVM for prediction
def predict(img, svm, hog_descriptor):
    img = cv2.resize(img, (64, 128))
    h = compute_hog_features(img, hog_descriptor)
    h = h.reshape(1, -1)
    _, result = svm.predict(h)
    return result[0][0]

# Load the trained SVM
svm = cv2.ml.SVM_load('hog_svm_model.yml')

# Predict on a new image
path_r = 'd1_4.png'
test_img_p = cv2.imread(path_r, cv2.IMREAD_GRAYSCALE)
result_p = predict(test_img_p, svm, hog)
result_txt =""
if result_p == 2:
    result_txt="d"
elif result_p == 1:
    result_txt="p"
else:
    result_txt="c"
print(result_txt)
in_test_img = cv2.imread(path_r, cv2.IMREAD_COLOR)
height, width, channel = in_test_img.shape
in_test_img = cv2.resize(in_test_img, dsize=(width*3,height*3), interpolation=cv2.INTER_LINEAR)
height, width, channel = in_test_img.shape
in_test_img = cv2.putText(in_test_img,result_txt, ( int(width/2), int(height/2)), cv2.FONT_HERSHEY_SIMPLEX,2, (0,255, 0), 2)
cv2.imshow('rectangle2',in_test_img)
cv2.waitKey(0)
cv2.destoryAllWindows()