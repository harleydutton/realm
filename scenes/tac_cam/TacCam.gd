extends Node3D

var SENSITIVITY_X = .005
func _input(event):
	if Input.is_action_pressed("pan") && event is InputEventMouseMotion:
		rotate_y(event.relative.x * SENSITIVITY_X)
