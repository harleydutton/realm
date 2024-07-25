using Godot;
using System;

public class Location : Node
{
	public Location(int x,int y,int z){
		this.x,this.y,this.z = x,y,z;
	}
	public int x {get;}
	public int y {get;}
	public int z {get;}
}