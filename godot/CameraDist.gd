extends SpringArm3D

var MAX_DIST = 20
var MIN_DIST = 0

func _input(event):
	if Input.is_action_pressed("zoom_out") && spring_length < MAX_DIST:
		spring_length+=1
	if Input.is_action_pressed("zoom_in") && spring_length > MIN_DIST:
		spring_length-=1
