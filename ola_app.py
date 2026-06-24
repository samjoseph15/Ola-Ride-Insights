import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="🚗 Ola Ride Insights 🚗",
    layout="wide"
)

st.title("🚗 Ola Ride Insights 🚗")

st.info("""
        This project analyzes 660,934 traffic crash records containing 39 variables related to crash outcomes,
injuries, roadway conditions, weather, lighting, traffic control devices, and geographic locations.

The goal is to identify key trends and insights to inform data-driven safety interventions and policies
that can reduce crash frequency and severity.
        """)

st.sidebar.title("📊 Dashboard Navigation")

analysis = st.sidebar.selectbox(
    "Select Analysis",
    [
        "All Successfull Bookings",
        "Average Ride Distance by Vehicle Type",
        "Cancelled Rides by Customers",
        "Cancelled Rides by Drivers - Reasons",
        "Max & Min Driver Ratings - Prime Sedan",
        "Payment Made Using UPI",
        "Average Customer Rating per Vehicle",
        "Total Booking Value of Successful Rides",
        "Incomplete Ride with Reason"
    ]
)


# Successfull Booking
if analysis == "All Successfull Bookings":
    st.subheader("a.All Succesfull Bookings")

    data = pd.DataFrame({
    "Booking_Status": ["Success"],
    "booking_counts": [63967]
})
    
    st.dataframe(data,use_container_width=True)

    st.success(""" 
               1. A total of 63,967 bookings were completed successfully.

               2. This indicates strong reliability and consistent ride completion performance.""")
    
    

#Avearge Distance   
elif analysis == "Average Ride Distance by Vehicle Type":
    st.subheader("b.Average Ride Distance by Vehicle Type")
    
    data = pd.DataFrame({
        "Vehicle_Type": ["Prime Sedan", "Bike", "Prime SUV", "eBike", "Mini", "Prime Plus", "Auto"],
        "avg_dist": [15.7649, 15.5331, 15.2745, 15.5806, 15.5101, 15.4475, 6.2381],
        "count": [14877, 14662, 14655, 14816, 14552, 14707, 14755]
        })
    
    st.dataframe(data,use_container_width=True)

    st.success("""
                1.Most vehicle types average around 15 km per ride, showing consistent usage patterns.

                2.Auto rides average only 6.2 km, highlighting their role in short, local trips.""")
    

#Cancelled by Riders
elif analysis == "Cancelled Rides by Customers":
    st.subheader("c.Cancelled Rides by Customers")

    data = ({
    "Canceled_Rides_by_Customer": [
        "Unknown",
        "Driver is not moving towards pickup location",
        "Driver asked to cancel",
        "Change of plans",
        "AC is Not working",
        "Wrong Address"],

    "count": [92525,3175,2670,2081,1568,1005] })

    st.dataframe(data,use_container_width=True)

    st.success("""
                1.Most cancellations (92,525) are marked as Unknown, showing limited feedback clarity.

                2. Operational issues like driver not moving (3,175) and driver asked to cancel (2,670) are notable specific reasons.""")
    

#Cancelled Driver   
elif analysis == "Cancelled Rides by Drivers - Reasons":
    st.subheader("d.Cancelled Rides by Drivers - Reasons")

    data = pd.DataFrame({
    "Canceled_Rides_by_Driver": [
        "Unknown",
        "Personal & Car related issue",
        "Customer related issue",
        "Customer was coughing/sick",
        "More than permitted people in there"
    ],
    "count": [
        84590,
        6542,
        5413,
        3654,
        2825
    ]
})
    
    st.dataframe(data,use_container_width=True)

    st.success(""" 
                1. Most cancellations (84,590) are marked as Unknown, limiting clarity on driver-side reasons.
               
                2.Specific issues like personal/car problems (6,542) and customer-related issues (5,413) are the main identifiable causes.""")
    

#Max and Min   
elif analysis == "Max & Min Driver Ratings - Prime Sedan":
    st.subheader("e.Max & Min Driver Ratings - Prime Sedan")

    data = pd.DataFrame({
    "Vehicle_Type": [
        "Prime Sedan", "eBike", "Auto", "Prime Plus", "Bike", "Prime SUV", "Mini"
    ],
    "count": [
        14877, 14816, 14755, 14707, 14662, 14655, 14552
    ]
})
    
    st.dataframe(data,use_container_width=True)

    st.success(""" 
                1.Prime Sedan (14,877) and eBike (14,816) have the highest booking counts, showing strong customer preference.
               
                2.Mini (14,552) records the lowest bookings, slightly trailing other vehicle types.""")
    

#Payment Methos  
elif analysis == "Payment Made Using UPI":
    st.subheader("f.Payment Made Using UPI")

    data =pd.DataFrame({
    "Vehicle_Type": ["Prime Sedan"],
    "Count": [14877],
    "max_driver_rating": [5.0],
    "min_driver_rating": [3.0]
})
    
    st.dataframe(data,use_container_width=True)

    st.success(""" 
                1.Prime Sedan has 14,877 bookings, making it a popular vehicle type.
               
                2.Driver ratings range from 3.0 to 5.0, showing both high satisfaction and some variability in service quality. """)
    


# Average Customer Rating per Vehicle
elif analysis == "Average Customer Rating per Vehicle":
    st.subheader("f.Average Customer Rating per Vehicle")

    data = pd.DataFrame({
    "Vehicle_Type": [
        "Prime Plus", "Prime Sedan", "Prime SUV", 
        "Auto", "Mini", "Bike", "eBike"
    ],
    "average_customer_rating": [
        4.005861, 4.001002, 3.999618, 
        3.999261, 3.998591, 3.995874, 3.992474
    ]
})
    st.dataframe(data,use_container_width=True)

    st.success(""" 
                1.Prime Plus (4.01) and Prime Sedan (4.00) have the highest average customer ratings, showing strong satisfaction.
               
                2.eBike (3.99) records the lowest rating, slightly trailing other vehicle types """)
    
# Total Booking Value of Successful Rides
elif analysis == "Total Booking Value of Successful Rides":
    st.subheader("g.Total Booking Value of Successful Rides")

    data = pd.DataFrame({
    "Booking_Status": ["Success"],
    "total_count": [63967]
})
    st.dataframe(data,use_container_width=True)

    st.success(""" 
                1.A total of 63,967 rides were successfully completed.
               
                2.This reflects strong reliability and consistent ride completion performance.""")


# Incomplete Ride with Reason   
elif analysis == "Incomplete Ride with Reason":
    st.subheader("h.Incomplete Ride with Reason")  

    data = pd.DataFrame({
    "Incomplete_Rides": [0.0],
    "total_count": [99098]
})
    st.dataframe(data,use_container_width=True)

    st.success(""" 
                1.A total of 99,098 rides were marked as incomplete.

                2.This highlights a significant portion of bookings that did not reach completion.""")




    
