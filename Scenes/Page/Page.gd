extends Node3D

var voxel = preload("res://Scenes/Page/Voxel.tscn")
var voxels = []

func _ready():
	add(Vector3(0,0,0))

func add(pos):
	var instance = voxel.instantiate()
	instance.position = pos
	voxels.append(instance)
	add_child(instance)
