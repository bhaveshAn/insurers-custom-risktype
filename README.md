# BriteCore VueApp

> A Vue.js project

## Decoupled Structure

- Flask Backend

- Vue.js Frontend

## Installation
 
``` bash

git clone https://github.com/bhaveshAn/iws-product-dev-eng-task.git
cd iws-product-dev-eng-task
 
# install dependencies
sudo pip install -r requirements.txt
npm install

# to run backend at localhost:5000
python backend/app.py

# to run frontend at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

## API Endpoints
``` bash

# GET and POST RiskType
http://localhost:5000/v1/risk_types

# Example Body for POST
{
"name": "Car"
}


# GET and POST Field
http://localhost:5000/v1/fields

# Example Body for POST
{
"name": "Tyres",
"type": "Integer",
"value": 4,
"risk_type_name": "Car"
}


# GET RiskTypeDetail
http://localhost:5000/v1/risk_type/<int:id>

# GET FieldDetail
http://localhost:5000/v1/field/<int:id>
```

## Screenshots

**1. E-R Diagram**

![E-R Diagram](https://image.ibb.co/ePKKWH/E_R_diagram.png)

**2. Homepage**

![Homepage](https://image.ibb.co/d184Fc/homepage.png)

**3. Car Risk Type**

![car](https://image.ibb.co/bB4yO7/car_new.png)

**4. House Risk Type**

![House](https://image.ibb.co/e7bOqn/house_new.png)

**5. Office Risk Type**

![Office](https://image.ibb.co/fVLzVn/office_new.png)

**6. Bicycle Risk Type**

![Bicycle](https://image.ibb.co/ko3Q37/bicycle_new.png)

**7. Prize Risk Type**

![Prize](https://image.ibb.co/jSm6An/prize_new.png)

**8. Table Risk Type**

![Table](https://image.ibb.co/eFC7GS/table_new.png)

**9. Chair Risk Type**

![Table](https://image.ibb.co/jJS4Vn/chair_new.png)

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).












