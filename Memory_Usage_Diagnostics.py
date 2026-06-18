        def om(self):
            #Memory diagnostics thingy i made #18.6.26-Raven
            #Note to self: remember to put the 'om' command in the no arguments list in the interpreter during usage, remember 
            #to remove all traces once done using :P
            import gc
            import os
            import psutil
            import tracemalloc

            if not tracemalloc.is_tracing():
                tracemalloc.start()

            process = psutil.Process(os.getpid())
            mem = process.memory_info()
            print("\n" + "=" * 70)
            print("MEMORY DIAGNOSTICS 2:--------------------------------------")
            print("=" * 70)

            print(f"RSS Memory      : {mem.rss / 1024 / 1024:.2f} MB")
            print(f"VMS Memory      : {mem.vms / 1024 / 1024:.2f} MB")
            try:
                print(f"GC Objects      : {len(gc.get_objects()):,}")
            except:
                pass
            print("\nINTERPRETER STATE")
            print("-" * 70)
            print(f"Call Stack      : {len(self.call_stack):,}")
            print(f"Control Stack   : {len(self.control_stack):,}")
            print(f"Variables       : {len(self.variables):,}")
            print(f"Local Variables : {len(self.local_variables):,}")
            print(f"Functions       : {len(self.functions):,}")
            print(f"Debug Log       : {len(self.debuglog):,}")
            print(f"Log Messages    : {len(self.log_messages):,}")

            print("\nGC GENERATIONS")
            print("-" * 70)
            print(f"Counts          : {gc.get_count()}")

            try:
                stats = gc.get_stats()

                print(
                    f"Gen0: collections={stats[0]['collections']} "
                    f"collected={stats[0]['collected']} "
                    f"uncollectable={stats[0]['uncollectable']}"
                )

                print(
                    f"Gen1: collections={stats[1]['collections']} "
                    f"collected={stats[1]['collected']} "
                    f"uncollectable={stats[1]['uncollectable']}"
                )

                print(
                    f"Gen2: collections={stats[2]['collections']} "
                    f"collected={stats[2]['collected']} "
                    f"uncollectable={stats[2]['uncollectable']}"
                )
            except:
                pass
            print("\nTOP MEMORY ALLOCATIONS")
            print("-" * 70)
            try:
                snapshot = tracemalloc.take_snapshot()
                for stat in snapshot.statistics("lineno")[:10]:
                    print(stat)
            except Exception as e:
                print("Tracemalloc Error:", e)
