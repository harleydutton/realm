using Godot;
using System;
using System.Collections.Generic;

public partial class Page : Node{
	private static PackedScene packedVoxel = ResourceLoader.Load<PackedScene>("res://Scenes/Page/Voxel.tscn");
	public List<Node3D> voxels;
	
	public Page(){
		voxels = new List<Node3D>();
	}
	
	public override void _Ready()
	{
		GD.Print("preparing to be ready!");
		add(new Vector3(0,0,0));
		GD.Print("ready!");
	}
	
	public void add(Vector3 pos){
		Node3D instance = (Node3D)packedVoxel.Instantiate();
		instance.Position = pos;
		voxels.Add(instance);
		AddChild(instance);
	}
	
	//public static CSharpScript MyNode { get; } =
		//GD.Load<CSharpScript>("res://Path/To/MyNode.cs");
	//public static PackedScene MyScene { get; } =
		//GD.Load<PackedScene>("res://Path/To/MyScene.tscn");
	
	//public Dictionary<(int,int,int),Object> voxels;
	//public Page(){
		//voxels = new Dictionary<(int,int,int),Object>();//use more specific generics
	//}
	//
	//public void addOne(int x, int y, int z){
		//var voxel = ResourceLoader.Load<PackedScene>("res://Data/Voxel.tscn").Instantiate();
		//ulong id = voxel.get_instance_id();
		//AddChild(voxel);
		//voxels.Add((x,y,z),id);//?
		//Object o = InstanceFromId(id);
		//o.position = (x,y,z);
		//GD.Print("added a voxel!");
	//}
	
	//public void procGen(){}
}
