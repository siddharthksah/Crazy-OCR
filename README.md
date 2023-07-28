# Crazy-OCR :eyes: :zap:
![Header](./header.png)
<p align="center">
  <a href="https://github.com/siddharthksah/Crazy-OCR/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/siddharthksah/Crazy-OCR"></a>
  <a href="https://github.com/siddharthksah/Crazy-OCR/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/siddharthksah/Crazy-OCR"></a>
  <a href="https://github.com/siddharthksah/Crazy-OCR/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/siddharthksah/Crazy-OCR"></a>
  <a href="https://github.com/siddharthksah/Crazy-OCR/blob/main/LICENSE.txt"><img alt="GitHub license" src="https://img.shields.io/github/license/siddharthksah/Crazy-OCR"></a>
</p>

Welcome to **Crazy-OCR**! :wave: Your one-stop destination for all your Optical character recognition(OCR) needs. This repository contains a robust and versatile OCR pipeline I developed while working on ID Cards for KYC. Feel free to explore, clone, or fork! 

## What's Inside :mag_right:
This repository houses a comprehensive set of OCR tools that I developed, including (but not limited to) the following features:

1. **Deskewing** :straight_ruler: - A useful tool for aligning images for better analysis.
2. **Edge detection** :triangular_ruler: - An algorithm designed to detect and highlight edges in your image.
3. **Contour Detection** :loop: - A feature that detects and isolates contours in your image.
4. **Rotation** :recycle: - A handy tool to adjust the orientation of your images.
5. **Adaptive Thresholding** :low_brightness: - This feature is to adjust the threshold level adaptively to make your image clearer.
6. **Multi image/file format compatibility** :file_folder: - Accepts and processes a wide variety of file formats for your convenience.
7. **Regex matching for FIN & DOB** :1234: - This tool helps in extracting and validating Financial Information Numbers (FIN) and Date of Birth (DOB) details.
8. **Interactive Morphing** :sparkles: - A feature to interactively morph your images.
9. **Interactive Image Intensity correction** :bulb: - An interactive tool to correct the intensity of your image for better visibility.
10. **Angle Correction** :level_slider: - This feature corrects any angular distortions in your images.
11. **Auto Deskew looping through an entire folder of images** :repeat: - Automates the deskewing process for a whole folder of images.
12. **ID CARD Image preprocessing** :credit_card: - A specific tool designed for pre-processing of ID card images.

All the files are extensively commented for your better understanding. Please refer to the code comments to know more about how specific files work. :notebook:

## How to Use :hammer_and_wrench:

Clone this repository to your local machine and run the scripts according to your requirements. Each script is independent and self-explanatory. Just make sure you have the required dependencies installed! If you have any issues, feel free to open an issue. :memo:

## Repository Contents :file_folder:

Here's a brief overview of the various scripts in the repository:

1. `common.py`: :wrench: - Commonly used functions and utilities.
2. `crop_id_card_using_edge_contour_detection.py`: :scissors: - Script to crop ID cards using edge and contour detection techniques.
3. `deskew_image_from_AC20_C20.py`: :straight_ruler: - A dedicated script to deskew images sourced from AC20_C20.
4. `deskew_image_rotate_loop.py`: :arrows_counterclockwise: - Script for deskewing and rotating images in a loop.
5. `deskew_loop_image_folder.py`: :file_folder: - A utility for deskewing all images in a given folder.
6. `id_card_detection_camera.py`: :camera: - Script to detect ID cards using a camera.
7. `id_card_dob_extractor.py`: :birthday: - A tool to extract DOB from ID cards.
8. `id_card_expiry_date_extractor.py`: :calendar: - Extracts the expiry date from ID cards.
9. `image_blurriness_detection.py`: :mag_right: - An image quality analysis tool focused on blurriness detection.
10. `image_deskewer.py`: :triangular_ruler: - A utility for deskewing single images.
11. `interactive_image_morphing.py`: :sparkles: - A tool for interactively morphing images.
12. `loop_through_morphed_images.py`: :repeat: - Utility to loop through morphed images.
13. `morphology_operations.py`: :loop: - Perform morphology operations for image processing.
14. `pdf2jpg.py`: :arrow_right: - Utility to convert PDF files to JPG.
15. `pdf_page_extractor.py`: :outbox_tray: - A script to extract specific pages from PDF files.
16. `photo_collage_maker.py`: :frame_photo: - A fun utility to create photo collages.
17. `preprocess_image.py`: :art: - A script for preliminary image processing.
18. `rotate_image_certain_angle.py`: :arrows_counterclockwise: - A utility to rotate images by a specified angle.
19. `show_image.py`: :framed_picture: - A script to display images.

Each file is extensively commented for better understanding. Refer to the code comments to know more about how specific files work. :notebook:

## Contributions :handshake:

Contributions are always welcomed. :smiley: If you have some ideas or improvements, feel free to make a pull request or open an issue to discuss it.

## License :page_facing_up:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements :star2:

I would like to thank my colleagues and everyone who contributed to making this project possible. :heart:

---

Enjoy using **Crazy-OCR**! :tada: Happy coding! :computer:
