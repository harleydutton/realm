extends Node3D

var PITCH_SENSITIVITY=.004

func _input(event):
	if Input.is_action_pressed("pan_button") && event is InputEventMouseMotion:
		rotate_x(event.relative.y * PITCH_SENSITIVITY)
		rotation.x=clamp(rotation.x,-PI/2,PI/2)
