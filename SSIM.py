import numpy as np
from PIL import Image
from scipy.signal import convolve2d


def matlab_style_gauss2D(shape=(3, 3), sigma=0.5):
	"""
    2D gaussian mask - should give the same result as MATLAB's
    fspecial('gaussian',[shape],[sigma])
    """
	m, n = [(ss - 1.) / 2. for ss in shape]
	y, x = np.ogrid[-m:m + 1, -n:n + 1]
	h = np.exp(-(x * x + y * y) / (2. * sigma * sigma))
	h[h < np.finfo(h.dtype).eps * h.max()] = 0
	sumh = h.sum()
	if sumh != 0:
		h /= sumh
	return h


def filter2(x, kernel, mode='same'):
	return convolve2d(x, np.rot90(kernel, 2), mode=mode)


def compute_ssim(im1, im2, k1=0.01, k2=0.03, win_size=11, L = 255):
	if not im1.shape == im2.shape:
		print("im1.shape", im1.shape)
		print("im2.shape", im2.shape)
		raise ValueError("Input Images must have the same dimensions")
	if len(im1.shape) > 2:
		print("im1.shape", im1.shape)
		print("len(im1.shape)", len(im1.shape))
		raise ValueError("Please input the images with 1 channel")

	M, N = im1.shape
	C1 = (k1 * L) ** 2
	C2 = (k2 * L) ** 2
	window = matlab_style_gauss2D(shape=(win_size, win_size), sigma=1.5)
	window = window / np.sum(np.sum(window))

	if im1.dtype == np.uint8:
		im1 = np.double(im1)
	if im2.dtype == np.uint8:
		im2 = np.double(im2)

	mu1 = filter2(im1, window, 'valid')
	mu2 = filter2(im2, window, 'valid')
	mu1_sq = mu1 * mu1
	mu2_sq = mu2 * mu2
	mu1_mu2 = mu1 * mu2
	sigma1_sq = filter2(im1 * im1, window, 'valid') - mu1_sq
	sigma2_sq = filter2(im2 * im2, window, 'valid') - mu2_sq
	sigmal2 = filter2(im1 * im2, window, 'valid') - mu1_mu2

	ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigmal2 + C2)) / ((mu1_sq + mu2_sq + C1) * (sigma1_sq + sigma2_sq + C2))

	return np.mean(np.mean(ssim_map))

if __name__ == "__main__":
	# Convert the image to a grayscale image
	im1 = Image.open("./normal.png").convert('L')
	im1.save('./garyNormal.png')
	im2 = Image.open("./abnormal.png").convert('L')
	im2.save('./garyAbnormal.png')
	im3 = Image.open("./normal2.png").convert('L')
	im3.save('./garyNormal2.png')
	im4 = Image.open("./abnormal2.png").convert('L')
	im4.save('./garyAbnormal2.png')
	im5 = Image.open("./normal.png").convert('L').save('./garyNormal.png')


	im1 = Image.open('./garyNormal.png')
	im2 = Image.open('./garyAbnormal.png')
	im3 = Image.open('./garyNormal2.png')
	im4 = Image.open('./garyAbnormal2.png')
	im5 = Image.open('./garyNormal.png')

	print("ssim between normal1 and abnormal1", compute_ssim(np.array(im1), np.array(im2)))
	print("ssim between normal2 and abnormal2", compute_ssim(np.array(im3), np.array(im4)))
	print("ssim between normal1 and normal2", compute_ssim(np.array(im1), np.array(im3)))
	print("ssim between abnormal1 and abnormal2", compute_ssim(np.array(im2), np.array(im4)))
	print("ssim between normal and normal", compute_ssim(np.array(im1), np.array(im5)))