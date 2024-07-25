using Godot;
using System;
using Player;


public class Page : Node
{
	public List<Player> players;
	public IDictionary<Location,Voxel> voxels;
	public Page(Player p){
		players.Add(p);
		voxels = new Dictionary<int, string>();//this should be Voxel.tscnS
	}
	
	//public void procGen(){}
}
