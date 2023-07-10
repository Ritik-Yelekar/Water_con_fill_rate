from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    node_name = request.form.get('node_name')
    tank_volume = float(request.form.get('tank_volume'))
    depth_tank = float(request.form.get('depth_tank'))
    breadth_tank = float(request.form.get('breadth_tank'))
    length_tank = float(request.form.get('length_tank'))
    upper_limit = float(request.form.get('upper_limit'))
    lower_limit = float(request.form.get('lower_limit'))
    fill_time = float(request.form.get('fill_time'))
    cons_time = float(request.form.get('cons_time'))

    print('Connecting to node ->', node_name)
    print('Connected, information is listed below')

    change_water_level = upper_limit - lower_limit
    print('Change in water level is:', change_water_level)

    tank_volume = tank_volume * 1000
    print('Tank volume is:', tank_volume)

    depth_tank = depth_tank * 100
    breadth_tank = breadth_tank * 100
    length_tank = length_tank * 100

    area_base = length_tank * breadth_tank
    vol_water = area_base * change_water_level / 1000
    print('Volume of water is:', vol_water)

    fill_rate = vol_water / fill_time
    print('Fill rate is:', fill_rate)

    vol_water_consumed = tank_volume - vol_water
    cons_rate = vol_water / cons_time
    print('Consumption rate is:', cons_rate)

    return render_template('index.html',
                           node_name=node_name,
                           change_water_level=change_water_level,
                           tank_volume=tank_volume,
                           vol_water=vol_water,
                           fill_rate=fill_rate,
                           vol_water_consumed=vol_water_consumed,
                           cons_rate=cons_rate)

if __name__ == '__main__':
    freezer.freeze()