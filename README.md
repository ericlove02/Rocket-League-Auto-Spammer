# Rocket-League-Auto-Spammer
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
<div id="top"></div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project  
I created this project as a birthday present to my brother, whom I play a lot of Rocket League with. The idea for the bot was basically just to fill up the chat while the player continues to play the game normally.   
I wanted to create a auto spam bot that would not impeed gameplay at all. Initially, I wrote a simple script that used PyAutoGui to listen for input and then repeat back preset input corresponding to the desired quick chat. With that method, the game would often lag as it waited for input, or struggled to catch up with unfinished, piled up outputs. To fix this issues, I switched to using the Keyboard library, linked below, and instead used a keyboard event to recieve a key, as opposed to waiting for a key constantly. I also added a boolean to check whether the previous output had been complete before starting a new one. The new method worked exactly as expected and now easily fills up game chats.    
To interface with the bot, I used tkinter. The program opens a window and prompts the user to enter the desired keybinds one by one, and then disappears when the entry is complete, with the script running in the background.

### Built With
* [tkinter](https://docs.python.org/3/library/tkinter.html)
* [PyAutoGui](https://pyautogui.readthedocs.io/en/latest/#)
* [Keyboard](https://github.com/boppreh/keyboard)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

```sh
   py install pip
   ```
### Installation
1. Download the [`main.exe`](https://github.com/ericlove02/Rocket-League-Auto-Spammer/tree/main/dist/main.exe) in yhr dist folder
#### or
1. Clone the repo
   ```sh
   git clone https://github.com/ericlove02/Rocket-League-Auto-Spammer.git
   ```
2. Install required packages
   ```sh
   pip install -r requirements.txt
   ```
3. Run `main.py`
   ```sh
   py main.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

https://user-images.githubusercontent.com/53005525/138221254-359a617d-b3fd-46d4-be8a-c9e8a8230ffc.mp4

<!-- CONTACT -->
## Contact

Eric Love - [LinkedIn](https://www.linkedin.com/in/ericlove02) - [eric.love02@yahoo.com](mailto:eric.love02@yahoo.com)

Project Link: [https://github.com/ericlove02/Valorant-Bot](https://github.com/ericlove02/Valorant-Bot)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[forks-shield]: https://img.shields.io/github/forks/ericlove02/Rocket-League-Auto-Spammer.svg?style=for-the-badge
[forks-url]: https://github.com/ericlove02/Rocket-League-Auto-Spammert/network/members
[stars-shield]: https://img.shields.io/github/stars/ericlove02/Rocket-League-Auto-Spammer.svg?style=for-the-badge
[stars-url]: https://github.com/ericlove02/Rocket-League-Auto-Spammer/stargazers
[issues-shield]: https://img.shields.io/github/issues/ericlove02/Rocket-League-Auto-Spammer.svg?style=for-the-badge
[issues-url]: https://github.com/ericlove02/Rocket-League-Auto-Spammer/issues
