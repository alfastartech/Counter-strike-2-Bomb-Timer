# Bomb Timer for Counter-Strike

This project implements a bomb timer for Counter-Strike, which activates upon detecting a certain amount of red pixels on the screen. The timer is displayed in a transparent window and starts when the red color threshold is reached.

## Functionality

- **Screen Scanning**: The program analyzes the upper part of the screen to detect red pixels.
- **Timer Activation**: The timer starts when the proportion of red pixels exceeds the specified threshold.
- **Timer Stopping**: The timer can be stopped if a white pixel is detected on the screen.

## Installation

1. Ensure you have Python 3.6 or newer installed.
2. Install the required dependencies:

    ```bash
    pip install pillow
    ```

## Running

To run the program, simply execute the script:

```bash
python your_script_name.py
Function Descriptions
get_red_pixel_ratio(image)
Returns the proportion of red pixels in the image.

Parameters:

image (PIL.Image): The image to analyze.
Returns:

float: The proportion of red pixels.
contains_white_pixel(image)
Checks if the image contains a white pixel.

Parameters:

image (PIL.Image): The image to analyze.
Returns:

bool: True if the image contains a white pixel, otherwise False.
start_timer(seconds, stop_event)
Starts a timer displayed in a transparent window. The timer stops if the stop_event is set.

Parameters:

seconds (int): The number of seconds for the timer countdown.
stop_event (threading.Event): An event to stop the timer.
scan_screen_and_start_timer(red_threshold=0.1)
Scans the screen for red pixels and starts the timer if the proportion of red pixels exceeds the specified threshold. Stops the timer if a white pixel is detected.

Parameters:

red_threshold (float): The threshold for the proportion of red pixels. If the proportion of red pixels exceeds this threshold, the timer starts.



Replace `your_script_name.py` with the actual name of your script file. Also, make sure to add a `LICENSE` file if you have one, and update the instructions accordingly.



# Таймер бомбы для игры Counter-Strike

Этот проект реализует таймер бомбы для игры Counter-Strike, который активируется при обнаружении определённого количества красных пикселей на экране. Таймер отображается в виде прозрачного окна и запускается при достижении порога красного цвета.

## Функциональность

- **Сканирование экрана**: Программа анализирует верхнюю часть экрана для обнаружения красных пикселей.
- **Запуск таймера**: Таймер запускается, когда доля красных пикселей превышает заданный порог.
- **Остановка таймера**: Таймер может быть остановлен, если обнаружен белый пиксель на экране.

## Установка

1. Убедитесь, что у вас установлен Python 3.6 или новее.
2. Установите необходимые зависимости:

    ```bash
    pip install pillow
    ```

## Запуск

Для запуска программы просто выполните скрипт:

```bash
python your_script_name.py
Описание функций
get_red_pixel_ratio(image)
Возвращает долю красных пикселей в изображении.

Параметры:

image (PIL.Image): Изображение для анализа.
Возвращает:

float: Доля красных пикселей.
contains_white_pixel(image)
Проверяет, содержит ли изображение белый пиксель.

Параметры:

image (PIL.Image): Изображение для анализа.
Возвращает:

bool: True, если изображение содержит белый пиксель, иначе False.
start_timer(seconds, stop_event)
Запускает таймер, который отображается в прозрачном окне. Таймер останавливается, если установлено событие stop_event.

Параметры:

seconds (int): Количество секунд для отсчёта таймера.
stop_event (threading.Event): Событие для остановки таймера.
scan_screen_and_start_timer(red_threshold=0.1)
Сканирует экран для обнаружения красных пикселей и запускает таймер, если доля красных пикселей превышает заданный порог. Останавливает таймер, если обнаружен белый пиксель.

Параметры:

red_threshold (float): Порог для доли красных пикселей. Если доля красных пикселей превышает этот порог, таймер запускается.
