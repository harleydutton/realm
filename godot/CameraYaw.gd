extends Node3D

var YAW_SENSITIVITY=.004

func _input(event):
	if Input.is_action_pressed("pan_button") && event is InputEventMouseMotion:
		rotate_y(event.relative.x * YAW_SENSITIVITY)
#
