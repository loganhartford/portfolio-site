---
name: CheatScore
tools: [Python, Google Places API, Tkinter]
image: https://res.cloudinary.com/dlfqn0wvp/image/upload/f_auto,q_auto/v1/portfolio-site/software/cheatscore/ln5kdi8phcssdx1oahfd
description: CheatScore is a Python application that helps users find nearby fast food meals based on their location and craving level.
slug: cheat-score
---

![Banner Image](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704580443/portfolio-site/software/cheatscore/a6a0mjns5gw5tghiv8d8.png)
<p class="post-metadata text-muted">
  August 17th, 2022
</p>
***
CheatScore is a Python application that helps users find nearby fast food meals based on their location and craving level. The app utilizes the Google Places API to retrieve nearby restaurant data and a local dataset for meal nutrition information. It allows users to input their location, set a search radius, and quantify their craving level on a scale of 1 to 10.

![Demo](https://github.com/loganhartford/cheat_meals/blob/main/demo/faster_demo.gif?raw=true)

The app provides users with a list of meal options from the selected restaurants, displaying them as cards with basic information. Users can click on a card to view detailed nutrition information, including caloric spread, caloric density, and a comparison of actual values to daily recommended values for various nutrients.

Additionally, the app provides a convenient button to open directions to the restaurant location using Google Maps.

{% include elements/button.html link="https://github.com/loganhartford/cheat_meals" text="GitHub" style="primary" size="lg" %}

## Screenshots

Here are some screenshots of CheatScore in action:
![Screenshot 1](https://res.cloudinary.com/dlfqn0wvp/image/upload/f_auto,q_auto/v1/portfolio-site/software/cheatscore/glbw2ruqi33io5oxfepd)

![Screenshot 2](https://res.cloudinary.com/dlfqn0wvp/image/upload/f_auto,q_auto/v1/portfolio-site/software/cheatscore/ln5kdi8phcssdx1oahfd)

## Features

- Location input: Users can enter their location in the form of an address.
- Radius selection: Users can set a search radius to find fast food restaurants within a specific distance from their location.
- Craving score: Users can quantify their craving level on a scale of 1 to 10, which helps in finding appropriate meal options.
- Restaurant search: The app uses the Google Places API to find fast food restaurants near the user's location.
- Meal options: The app displays a list of meal options from the selected restaurants as cards, showing basic information.
- Detailed nutrition information: Users can click on a card to view detailed nutrition information for a specific meal, including caloric spread, caloric density, and a comparison of actual values to daily recommended values for various nutrients.
- Directions: The app provides a button to open directions to the restaurant location using Google Maps.

## Setup

1. Clone the repository or download the source code.
2. (Optional) Create and activate a virtual environment using your preferred method.
3. Install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

4. Run the application by executing the `main.py` file:

```
python main.py
```

Alternatively, you can use the provided executable file, but ensure that the dependencies are present in the same folder. The executable file will only work on windows operating systems.

## Future Improvements

- Enhanced search functionality: Implement advanced search options, such as filtering by specific nutrients or dietary requirements.
- User preferences and profiles: Allow users to save their preferences and create profiles to personalize the app experience.
- User interface enhancements: Improve the user interface by adding more interactive features, better styling, and visualizations.


